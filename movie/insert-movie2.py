import tkinter as tk
from tkinter import messagebox
from connection import get_connection

def insert_movie(title, year, zanra):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO movies (title, year, zanra) VALUES (%s, %s, %s)"
        values = (title, year, zanra)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print("ΣΦΑΛΜΑ:", e)
        return False

def fetch_movies():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT id, title, year, zanra FROM movies"
        cursor.execute(sql)
        movies = cursor.fetchall()
        cursor.close()
        connection.close()
        return movies
    except Exception as e:
        print("ΣΦΑΛΜΑ κατά την ανάκτηση:", e)
        return []

def submit_movie():
    title = entry_title.get()
    year = entry_year.get()
    zanra = entry_zanra.get()

    if not (title and year and zanra):
        messagebox.showwarning("ΣΦΑΛΜΑ", "Συμπληρώστε όλα τα πεδία")
        return

    try:
        year = int(year)
    except ValueError:
        messagebox.showwarning("ΣΦΑΛΜΑ", "Το έτος πρέπει να είναι αριθμός")
        return

    if insert_movie(title, year, zanra):
        messagebox.showinfo("ΕΠΙΤΥΧΙΑ", "Η ταινία προστέθηκε επιτυχώς!")
        entry_title.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_zanra.delete(0, tk.END)
    else:
        messagebox.showerror("ΣΦΑΛΜΑ", "Απέτυχε η καταχώρηση")

def view_movies():
    movies = fetch_movies()
    text_display.delete("1.0", tk.END)
    if not movies:
        text_display.insert(tk.END, "Δεν υπάρχουν καταχωρημένες ταινίες.\n")
    else:
        for movie in movies:
            text_display.insert(tk.END, f"id: {movie[0]}\nΤίτλος: {movie[1]}\nΈτος: {movie[2]}\nΕίδος: {movie[3]}\n\n")

root = tk.Tk()
root.title("Εισαγωγή Ταινίας")
root.geometry("500x600")

tk.Label(root, text="Τίτλος:").pack(pady=6)
entry_title = tk.Entry(root, width=40)
entry_title.pack()

tk.Label(root, text="Έτος:").pack(pady=6)
entry_year = tk.Entry(root, width=40)
entry_year.pack()

tk.Label(root, text="Είδος:").pack(pady=6)
entry_zanra = tk.Entry(root, width=40)
entry_zanra.pack()

submit_button = tk.Button(root, text="Καταχώρηση Ταινίας", command=submit_movie)
submit_button.pack(pady=20)

view_button = tk.Button(root, text="Προβολή όλων των Ταινιών", command=view_movies)
view_button.pack(pady=5)

text_display = tk.Text(root, height=15, width=60)
text_display.pack(pady=10)

root.mainloop()
