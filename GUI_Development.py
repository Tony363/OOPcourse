import tkinter as tk
import webbrowser
# from tkinter import ttk

def doorbell(event):
    print("you rang the doorbell!")

def fuckyou(event):
    print("fuckyou")

def link(event):
    webbrowser.open_new_tab("www.google.com")
    
window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0,row=0)

blabel = tk.Label(text="Apple")
blabel.grid(column= 1, row=0)

button = tk.Button(window, text="doorbell")
button.grid(column=0, row=1)
button.bind("<Button-1>", doorbell)

button2 = tk.Button(window, text="10")
button2.grid(column=1, row=1)
button2.bind("<Button-1>", fuckyou)

button3 = tk.Button(text="google.com")
button3.grid(column=2, row=1)
button3.bind("<Button-1>", link)

window.mainloop()
