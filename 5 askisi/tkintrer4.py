import tkinter as tk 

def show_selection():
    label.config(text=f"Επιλογη:{var.get()}")
    
root = tk.Tk()
root.title("RadioButtons")
root.geometry("400x400")

var = tk.StringVar(value="Καμια Επιλογη")

radio1 = tk.Radiobutton(root, text="Ανδρας", variable=var,value="Ανδρας", command=show_selection)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Γυνακα", variable=var,value="Γυνακα", command=show_selection)
radio2.pack()

radio3 = tk.Radiobutton(root, text="Αλλο", variable=var,value="Αλλο", command=show_selection)
radio3.pack()


label = tk.Label(root, text="Epilogi", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
