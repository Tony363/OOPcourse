from tkinter import *
import sqlite3

root = Tk()
root.title("My Bookmarks!")
root.geometry("400x400")

# create a datase or connect to one
conn = sqlite3.connect('bookmarks.db')

# create cursor
cursor = conn.cursor()

#create table
#cursor.execute("""CREATE TABLE bookmarks (textbox text)""")

def links():
    # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    #Query database
    cursor.execute("SELECT *, oid FROM bookmarks")
    marks = cursor.fetchall()
    print(marks)


    print_marks = ''
    for mark,r in enumerate(marks,6):
        
        
        print_marks += str(mark) + "\n"

        extension = Button(root, text=print_marks)
        extension.grid(row=r, column=0, columnspan=3)

        print_marks = print_marks - str(mark) + "\n"


    # Commit Changes
    conn.commit()

    # close connection
    conn.close()

    

#create submit function for database
def submit():
    # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    #insert into table
    cursor.execute("INSERT INTO bookmarks VALUES (:textbox )",
                    {
                        'textbox': textbox.get()
                    }
                    )

    # Commit Changes
    conn.commit()

    # close connection
    conn.close()
    




textbox = Entry(root, width=30)
textbox.grid(row=0, column=1, padx=20)

#Craete text box Labels
textLabel = Label(root, text="enter link")
textLabel.grid(row=0, column=0)

#create button for text box

sbt = Button(root, text="Add Book Marks!", command=submit)
sbt.grid(row=0, column=2, pady=10, padx=10)

#create a link button
linkbtn = Button(root, text="links", command=links)
linkbtn.grid(row=1, column=0, columnspan=4, pady=10, padx=10, ipadx=137)

#Commit Changes
conn.commit()

# close connection
conn.close()

root.mainloop()