import tkinter as tk 

def say_hello():
    label.config(text="koumpi patithike!")

root = tk.Tk()

root.title("Label Widget")

root.geometry("400x400")

label = tk.Label(root, text="patithike to koubi", font=("Arial", 14))
label.pack(pady=20)  # Correctly packed once

button = tk.Button(root, text="pata me", command=say_hello, font=("Arial", 14), bg="black", fg="white")
button.pack(pady=10)  # <- You forgot to pack the button

root.mainloop()
