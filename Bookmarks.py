import tkinter as tk
import webbrowser

from tkinter import *
# from tkinter import ttk

window = tk.Tk()
window.geometry("400x200")

e = Entry(window, width=35, borderwidth=5)
e.grid(column=0, row=0, columnspan=3)
entry = tk.Entry()
entryString = entry.get()

def addBookmark(event):
    Bookmark = tk.Button(window,text="{}".format(entryString))
    Bookmark.grid(column=0,row=1)
    # def gridButton(event):
    #     column = 0
    #     for i in 







add_bookmark = tk.Button(window,text="Add Bookmark")
add_bookmark.grid(column=5,row=0)
add_bookmark.bind("<Button-1>", addBookmark)

window.mainloop()