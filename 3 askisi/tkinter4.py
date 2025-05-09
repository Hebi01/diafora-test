import tkinter as tk 

root = tk.Tk()

root.title("First App With Tkinter")

root.geometry("400x400")

# Fix: 'button' should be 'Button'
exit_button = tk.Button(root, text="Close", command=root.quit)

exit_button.pack(pady=20)

root.mainloop()
