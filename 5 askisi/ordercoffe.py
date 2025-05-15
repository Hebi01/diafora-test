import tkinter as tk 


def calculate_price():
    price = 0
    if coffe_type.get() == "Espresso":
        price = 2.0
    elif coffe_type.get() == "Cappucino":
        price = 3.0
    elif coffe_type.get() == "Latte":
        price = 3.5
        
    if size.get() == "Megalo":
        price += 1 
        
    if suger.get():
        price += 0.5
    if milk.get():
        price += 0.5
        
    
    Label_price.config(text=f"Sunoliko kostos: {price:.2f}€")
            




root = tk.Tk()
root.title("Order Coffe")
root.geometry("440x400")

coffe_type = tk.StringVar(value="Espresso")
tk.Label(root,text="Epilexe kafe",font=("Arial",12)).pack()
tk.Radiobutton(root,text="Espresso 2€", variable=coffe_type, value="Espresso").pack()
tk.Radiobutton(root,text="Cappucino 3€", variable=coffe_type, value="Cappucino").pack()
tk.Radiobutton(root,text="Latte 3.5€", variable=coffe_type, value="Latte").pack()


size = tk.StringVar(value="Mikro")
tk.Label(root,text="Megethos:",font=("Arial",12)).pack()
spinbox = tk.Spinbox(root, values=("Mikro","Megalo"))
spinbox.pack()


suger = tk.IntVar()
milk = tk.IntVar()
tk.Checkbutton(root,text="zaxari +0.5€",variable=suger).pack()
tk.Checkbutton(root,text="Gala +0.5€",variable=milk).pack()

tk.Button(root,text="Ypologisomos",command=calculate_price,font=("Arial",14),bg="brown",fg="white").pack(pady=10)

Label_price = tk.Label(root,text="Sunoliko kostos: 00.0",font=("Arial",14))
Label_price.pack()

root.mainloop()
