import datetime
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter import *
from PIL import ImageTk, Image
import os



root = Tk()
root.title("Age calculator!")
root.geometry("400x400")

img = ImageTk.PhotoImage(Image.open("2979-200.png"))
panel = Label(root, image = img)
panel.grid(column=1, row=0)
def calculateAge():
    # birthday = "{},{},{}".format(yearEntry.get(),monthEntry.get(),dayEntry.get())
    # print(birthday)
    birthdayOject = datetime.strptime( str(monthEntry.get()) + " " +  str(dayEntry.get()) + " " + str(yearEntry.get()), '%b %d %Y') 
    today_date = datetime.today()
    age = today_date.year - birthdayOject.year
    ageL = Label(root, text="Your age is " + str(age))
    ageL.grid(column=1, row=6)
    
   

yearL = Label(root, text='Year:')
yearL.grid(column=0,row=1)
yearEntry = Entry(root)
yearEntry.grid(column=1,row=1)

monthL = Label(root,text='Month:')
monthL.grid(column=0, row=2)
monthEntry = Entry(root)
monthEntry.grid(column=1,row=2)

dayL = Label(root, text='Day:')
dayL.grid(column=0, row=3)
dayEntry = Entry(root)
dayEntry.grid(column=1,row=3)

calculateB = Button(root,text='Calculate Now!', command=calculateAge)
calculateB.grid(column=1, row=4, padx=30)

root.mainloop()

