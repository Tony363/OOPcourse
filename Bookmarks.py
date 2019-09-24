import tkinter as tk
import webbrowser

from tkinter import *
# from tkinter import ttk

window = tk.Tk()
window.geometry("400x200")



global Button_Count
Button_Count = 0

entry_id = StringVar() # create an id for your entry, this helps getting the text
entry = tk.Entry(window, textvariable=entry_id, justify=RIGHT)
entry.grid(row=0, column=1, sticky=E)





def addBookmark(event):
    # get the text from entry
    
    Bookmark = StringVar()
    invisible = tk.Button(window, text='', textvariable=Bookmark)
    invisible.grid(row=1, column=1, sticky=W)
    reply = Bookmark.set(format(entry_id)) # format the text on the invisible label you created above
		
    def clickcount():
        global Button_Count
        Button_Count += 1
    
    # Bookmark.grid(column=0,row=Button_Count)
    return reply
 

add_bookmark = tk.Button(window,text="Add Bookmark")
add_bookmark.grid(column=5,row=0)
add_bookmark.bind("<Button-1>", addBookmark)

window.mainloop()