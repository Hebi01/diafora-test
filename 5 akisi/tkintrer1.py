import tkinter as tk 

def show_selection():
    label.config(text=f"Επιλογή: {var.get()}")

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

var = tk.StringVar(value="Καμία επιλογή")

radio1 = tk.Radiobutton(root, text="Επιλογή 1", variable=var, value="Επιλογή 1", command=show_selection)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Επιλογή 2", variable=var, value="Επιλογή 2", command=show_selection)
radio2.pack()

label = tk.Label(root, text="Καμία επιλογή", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
