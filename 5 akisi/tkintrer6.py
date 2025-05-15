import tkinter as tk 

def show_value():
    label.config(text=f"Epiligi: {spinbox.get()}")
    
root = tk.Tk()
root.title("spinbox")
root.geometry("400x400")

spinbox = tk.Spinbox(root,from_=1,to=100,command=show_value)
spinbox.pack(pady=10)

label = tk.Label(root,text="Epilogi: 0",font=("Arial",14))
label.pack(pady=10)

root.mainloop()   