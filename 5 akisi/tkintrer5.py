import tkinter as tk 

def update_label(value):
    label.config(text=f"Τιμη: {value}")
    
root = tk.Tk()
root.title("Scale Windget")
root.geometry("400x400")

scale = tk.Scale(root,from_=0,to=100,orient="horizontal",command=update_label)
scale.pack(pady=10)

label = tk.Label(root,text="Timh: 0",font=("Arial",14))
label.pack()

root.mainloop()