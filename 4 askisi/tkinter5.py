import tkinter as tk


root = tk.Tk()
root.title("ola ta widges")
root.geometry("400x400")

frame = tk.Frame(root,bg="orange",padx=10,pady=10)
frame.pack(pady=10)

label = tk.Label(frame, text="Auto einai ena freme",font=("Arial",12))
label.pack()

button = tk.Button(frame, text="click")
button.pack()

root.mainloop()
