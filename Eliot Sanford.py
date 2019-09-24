import tkinter as tk

def make_label(event):
    alabel = tk.Label(window, text="Nice job!")
    alabel.grid(column=2, row=3)

def second_button(event):
    button2 = tk.Button(window, text = "Click here again.")
    button2.grid(column=2)
    button2.bind("<Button-1>", make_label)

window = tk.Tk()
window.geometry ("500x250")

button = tk.Button(window, text="Click here.")
button.grid(column=0)

button.bind("<Button-1>", second_button)

window.mainloop()