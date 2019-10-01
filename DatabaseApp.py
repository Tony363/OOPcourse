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

#function that update the editor
def update():
     # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    record_id = selectbox.get()
    cursor.execute("""UPDATE bookmarks SET 
                textbox = :site  
                WHERE oid = :oid""",
                   {
                    'site':textbox_editor.get(),
                    'oid':record_id
                    }
                )

    #Commit Changes
    conn.commit()

    # close connection
    conn.close()

    editor.destroy()

    

#create function to edit a record
def edit():
    global editor
    editor = Tk()
    editor.title("Update!")
    editor.geometry("400x400")

    #create global textbox from editor
    global textbox_editor

    textbox_editor = Entry(editor, width=30)
    textbox_editor.grid(row=0, column=1, padx=20)

    textLabel_editor = Label(editor, text="update link")
    textLabel_editor.grid(row=0, column=0)

    sbt_editor = Button(editor, text="Update!", command=update)
    sbt_editor.grid(row=0, column=2, pady=10, padx=10)

    # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    record_id = selectbox.get()
    
    #Query database
    cursor.execute("SELECT * FROM bookmarks WHERE oid = " + record_id)
    marks = cursor.fetchall()
    print(marks)

    #loop through results
    for mark in marks:
        textbox_editor.insert(0, marks[0])
  
  


#create function to delete a record
def delete():
    # create a datase or connect to one
    conn = sqlite3.connect('bookmarks.db')

    # create cursor
    cursor = conn.cursor()

    #Query database
    cursor.execute("DELETE FROM Bookmarks WHERE oid = ? ", selectbox.get() )

    #Commit Changes
    conn.commit()

    # close connection
    conn.close()

#create links to webbrowser
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

        extension = Button(root, text= str(i) + " " + mark, command=openchrome)
        #extension.delete(0,END)
        extension.grid(row=i+4, column=0, columnspan=3)
    

    # Commit Changes
    conn.commit()

    # close connection
    conn.close()


    

#create submit function for database
def addbookmarks():
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
selectbox = Entry(root, width=30)
selectbox.grid(row=2, column=1)


#Create text box Labels
textLabel = Label(root, text="enter link")
textLabel.grid(row=0, column=0)
selectLabel = Label(root, text="select link")
selectLabel.grid(row=2, column=0)

#create button for text box

sbt = Button(root, text="Add Book Marks!", command=addbookmarks)
sbt.grid(row=0, column=2, pady=10, padx=10)

#create a link button
linkbtn = Button(root, text="Links", command=links)
linkbtn.grid(row=1, column=0, columnspan=4, pady=10, padx=10, ipadx=137)

#create a delete button
deletebtn = Button(root, text="Delete", command=delete)
deletebtn.grid(row=3, column=0, columnspan=4, pady=10, padx=10, ipadx=135)

#create an update button
Editbtn = Button(root, text="Edit", command=edit)
Editbtn.grid(row=4, column=0, columnspan=4, pady=10, padx=10, ipadx=143)



#Commit Changes
conn.commit()

# close connection
conn.close()

root.mainloop()