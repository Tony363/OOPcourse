from tkinter import *
import sqlite3
import webbrowser

root = Tk()
root.title("My Bookmarks!")
root.geometry("400x400")

# create a datase or connect to one
conn = sqlite3.connect('bookmarks.db')

# create cursor
cursor = conn.cursor()

#create table
#cursor.execute("""CREATE TABLE bookmarks (textbox text)""")

#create function to delete a record

def delete():
    # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    #Query database
    cursor.execute("DELETE FROM Bookmarks WHERE value =? ", deletebox.get() )

    #Commit Changes
    conn.commit()

    # close connection
    conn.close()


def links():
    # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    #Query database
    cursor.execute("SELECT *, oid FROM bookmarks")
    marks = cursor.fetchall()
    print(marks)
  
    for mark, i in marks:
        def openchrome():
            webbrowser.open_new_tab(mark)

        extension = Button(root, text=mark, command=openchrome)
        extension.grid(row=i+3, column=0, columnspan=3)

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
deletebox = Entry(root, width=30)
deletebox.grid(row=2, column=1)


#Craete text box Labels
textLabel = Label(root, text="enter link")
textLabel.grid(row=0, column=0)
deleteLabel = Label(root, text="delete link")
deleteLabel.grid(row=2, column=0)

#create button for text box

sbt = Button(root, text="Add Book Marks!", command=submit)
sbt.grid(row=0, column=2, pady=10, padx=10)

#create a link button
linkbtn = Button(root, text="Links", command=links)
linkbtn.grid(row=1, column=0, columnspan=4, pady=10, padx=10, ipadx=137)

#create a delete button
deletebtn = Button(root, text="Delete", command=delete)
deletebtn.grid(row=3, column=0, columnspan=4, pady=10, padx=10, ipadx=135)



#Commit Changes
conn.commit()

# close connection
conn.close()

root.mainloop()