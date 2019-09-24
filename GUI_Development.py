import tkinter as tk
import webbrowser
# from tkinter import ttk

def doorbell(event):
    print("you rang the doorbell!")

def fuckyou(event):
    print("fuckyou")

def CP(event):
    webbrowser.open_new_tab("https://medium.com/cleverprogrammer")

def hey_abdallah(event):
    webbrowser.open_new_tab("https://medium.com/@selfengineeredd")

window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="clicky")
alabel.grid(column=0,row=0)
button = tk.Button(window, text="doorbell")
button.grid(column=0, row=1)
button.bind("<Button-1>", doorbell)

blabel = tk.Label(text="WTF")
blabel.grid(column= 1, row=0)
button2 = tk.Button(window, text="hey")
button2.grid(column=1, row=1)
button2.bind("<Button-1>", fuckyou)

button3 = tk.Button(window,text="google.com")
button3.grid(column=2, row=1)
button3.bind("<Button-1>", CP)

blogpost = tk.Label(text="Self engineered")
blogpost.grid(column=0,row=2)
blogButton = tk.Button(window,text="Posts")
blogButton.grid(column=0,row=3)
blogButton.bind("<Button-1>", hey_abdallah)



window.mainloop()
