import tkinter as tk 

root = tk.Tk()

root.title("Label Widget")

root.geometry("400x400")

label = tk.Label(root, text="geia", font=("Arial", 16), fg="red")

label.pack(pady=10)  # Fixed: changed pady_10 to pady=10

root.mainloop()
