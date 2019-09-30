import datetime
import tkinter as tk
from datetime import date
from dateutil.relativedelta import relativedelta

# rdelta = relativedelta(date.today(),datetime.date(1996,5,6))
# print('Age in years: ', rdelta.years)

# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
# print(datetime_object)

#create frame
window = tk.Tk()

#create frame geometry
window.geometry("400x400")

#set the title of the frame
window.title("Age Calculator APP")

#adding labels
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)

calculate_button = tk.Button(window,text='Calculate Now')
calculate_button.grid(column=1, row=4)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    # def Age(self, age, birthdate):
    #     age = relativedelta(date.today(), self.birthdate)
    #     print("{}".format(age))
    #     return self.age 
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age
    def __str__(self):
        return "{}".format(age)

trial = date.today() - datetime.date(1996,5,6)
print(trial)

Tony = Person("Tony", datetime.date(1996,5,6))
print(Tony.name + ":" + str(Tony.birthdate) + "," + "Age being " + str(Tony.age()))
# print(Tony.age())



window.mainloop()