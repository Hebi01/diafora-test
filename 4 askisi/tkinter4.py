import tkinter as tk

def show_text():
    text = entry.get()
    textarea.insert(tk.END, text + "\n")  # Προσθέτω και αλλαγή γραμμής για κάθε νέα είσοδο

root = tk.Tk()
root.title("Tkinter 3")
root.geometry("400x400")

label = tk.Label(root, text="graxe kati:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

button = tk.Button(root, text="click", command=show_text, font=("Arial", 12), bg="black", fg="white")
button.pack(pady=10)

textarea = tk.Text(root, font=("Arial", 12), height=5, width=30)
textarea.pack(pady=10)

root.mainloop()
