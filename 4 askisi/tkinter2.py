import tkinter as tk

def get_text():
    text = entry.get()
    label.config(text=f"{text}")

root = tk.Tk()

root.title("O titlos pou dino sto parathiro mou")
root.geometry("500x600")

label = tk.Label(root, text=" graye kati kai pata to kuby " ,font=("Arial", 16))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=20)
entry.pack(pady=5)

button1 = tk.Button(root, text="OK", command=get_text, font=("Arial", 18), bg="Green", fg="white")
button1.pack(pady=10)

root.mainloop()
