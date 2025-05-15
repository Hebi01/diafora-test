import tkinter as tk

def show_selection():
    selected = []
    
    if var1.get():
        selected.append("Kafe")
    if var2.get():
        selected.append("Chai")
    if var3.get():
        selected.append("Ximo")
     
    label.config(text="Epiloges: " + ", ".join(selected))


root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("400x400")

# Define variables
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()


chk1 = tk.Checkbutton(root, text="Kafe", variable=var1, command=show_selection)
chk1.pack()

chk2 = tk.Checkbutton(root, text="Chai", variable=var2, command=show_selection)
chk2.pack()

chk3 = tk.Checkbutton(root, text="Ximo", variable=var3, command=show_selection)
chk3.pack()

label = tk.Label(root, text="Epilogi", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
