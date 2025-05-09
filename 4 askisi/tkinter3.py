import tkinter as tk

def get_text():
    text = textbox.get("1.0", tk.END)
    label.config(text=f"to mikos einai: {len(text.strip())}")  # strip για να αφαιρέσουμε τα περιττά κενά

root = tk.Tk()
root.title("Tkinter 3")
root.geometry("400x400")

label = tk.Label(root, text="graxe kati:", font=("Arial", 16))
label.pack(pady=5)

textbox = tk.Text(root, font=("Arial", 12), height=5, width=30)
textbox.pack(pady=10)

button = tk.Button(root, text="ypologismos", command=get_text, font=("Arial", 12))
button.pack(pady=5)

root.mainloop()
