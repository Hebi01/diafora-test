import tkinter as tk 

root = tk.Tk()
root.title("Grid")
root.geometry("400x400")

label1 = tk.Label(root,text="Ovoma")
label1.grid(row=0,column=0,padx=5,pady=5)

entry1 = tk.Entry(root)
entry1.grid(row=0,column=1,padx=5,pady=5)

label2 = tk.Label(root,text="epitheto")
label2.grid(row=1,column=0,padx=5,pady=5)


entry2 = tk.Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)

button = tk.Button(root,text="send")
button.grid(row=2,column=0,columnspan=2,pady=10)

root.mainloop()