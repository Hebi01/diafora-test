import tkinter as tk

def show_selection():
    label.config(text=f"Epilogi:{var.get()}")
    
root = tk.Tk()

root.title("keckbutton")
root.geometry("400x400")

var = tk.IntVar()

check = tk.Checkbutton(root,text="simfono",variable=var, command=show_selection)
check.pack(pady=10)

label = tk.Label(root, text="kamia epilogi",font=("Arial",12))
label.pack(pady=10)

root.mainloop()