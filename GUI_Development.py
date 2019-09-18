import tkinter as tk
# from tkinter import ttk

def doorbell(event):
    print("you rang the doorbell!")
window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0,row=0)

blabel = tk.Label(text="Apple")
blabel.grid(column= 1, row=0)

button = tk.Button(window, text="doorbell")
button.grid(column=0, row=1)

button2 = tk.Button(window, text="10")
button2.grid(column=1, row=1)

button.bind("<Button-1>", doorbell)

window.mainloop()
