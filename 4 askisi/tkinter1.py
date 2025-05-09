import tkinter as tk

def hello():
    epiketa.config(text="to koumpi patithike")
    
def get_text():
    text = entry.get()
    tag.config(text=f"{text}")

root = tk.Tk()

root.title("O titlos pou dino sto parathiro mou")

root.geometry("500x600")
root.minsize(400, 400)
root.maxsize(900, 700)

root.configure(bg="teal")


exit_button = tk.Button(root, text="Close", command=root.quit)
exit_button.pack(pady=20)


label = tk.Label(root, text="geia sou", font=("Arial", 16), fg="red")
label.pack(pady=10)


epiketa = tk.Label(root, text="patise to koubi", font=("Arial", 14))
epiketa.pack(pady=10)


button = tk.Button(root, text="pata me", command=hello, font=("Arial", 14), bg="white", fg="orange")
button.pack(pady=10)


tag = tk.Label(root, text=" graye kati kai pata to kuby " ,font=("Arial", 16))
tag.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=20)
entry.pack(pady=5)

entry = tk.Entry(root, font=("Arial",20),width=5)


button1 = tk.Button(root, text="OK", command=get_text, font=("Arial", 18), bg="Green", fg="white")
button1.pack(pady=10)

root.mainloop()
