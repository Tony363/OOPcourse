class Student:
    def __init__(self, name, grade, age):
        self.age = age
        self.name = name
        self.grade = grade


kitty = Student('Kitty',30, 85)
daniel = Student('Daniel', 80, 15)

print(kitty.name, kitty.grade,daniel.name,daniel.grade)

print(kitty.age, daniel.age)
