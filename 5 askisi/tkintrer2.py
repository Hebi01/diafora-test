import tkinter as tk 

def show_text():
    text =entry.get()
    label2.config(text=f"Keimeno:{text}")


root = tk.Tk()
root.title("Frame")
root.geometry("300x400")


Frame1= tk.Frame(root,bg="lightblue",padx=10,pady=10) 
Frame1.pack(pady=10)

label = tk.Label(root, text="Graxe kati", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, text="Graxe kati", font=("Arial", 12))
entry.pack(pady=10)

Frame2 = tk.Frame(root,bg="lightblue",padx=10,pady=10) 
Frame2.pack(pady=10)

button = tk.Button(Frame2,text="show",command=show_text) 
button.pack()

label2 = tk.Label(Frame2,text="apotelesma",font=("Arial",14))
label2.pack()

root.mainloop()
