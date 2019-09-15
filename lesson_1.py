class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
kitty = Student('Kitty', 85)
daniel = Student('Daniel', 80)

print(kitty.name)
print(daniel.name)
print(kitty.grade)
print(daniel.grade)
