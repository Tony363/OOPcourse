from tkinter import *
import sqlite3

root = Tk()
root.title("My Bookmarks!")
root.geometry("400x400")

# create a datase or connect to one
conn = sqlite3.connect('book_marks.db')

# create cursor
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE book_marks (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

#Commit Changes
conn.commit()

# close connection
conn.close()

root.mainloop()