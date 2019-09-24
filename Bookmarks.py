import tkinter as tk
import webbrowser

from tkinter import *
# from tkinter import ttk

window = tk.Tk()
window.geometry("400x200")

entry_id = StringVar() # create an id for your entry, this helps getting the text
entry = tk.Entry(window, textvariable=entry_id, justify=RIGHT)
entry.grid(row=0, column=1, sticky=E)





def addBookmark(event):
    # get the text from entry
    
    Bookmark = StringVar()
    invisible = tk.Button(window, text='', textvariable=Bookmark)
    invisible.grid(row=1, column=1, sticky=W)
     
    def clicked():
	    text = entry_id.get() # get the text from entry
		reply = Bookmark.set(format(text)) # format the text on the invisible label you created above
		return reply
    

add_bookmark = tk.Button(window,text="Add Bookmark")
add_bookmark.grid(column=5,row=0)
add_bookmark.bind("<Button-1>", addBookmark)

window.mainloop()