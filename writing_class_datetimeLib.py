import datetime
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

# rdelta = relativedelta(date.today(),datetime.date(1996,5,6))
# print('Age in years: ', rdelta.years)

# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
# print(datetime_object)

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


Tony = Person("Tony", datetime.date(1996,5,6))
print(Tony.name + ":" + str(Tony.birthdate) + "," + "Age being " + str(Tony.age()))
# print(Tony.age())

# trial = date.today() - datetime.date(1996,5,6)
# print(trial)
