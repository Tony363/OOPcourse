class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        return "fuck" + " " + "you"

pet_qazi = Animal("Qazoo")
print(pet_qazi.name, pet_qazi.talk())
class Dog(Animal):
    def talk(self):
        return "woof"

class Cat(Animal):
    def talk(self):
        return "mweoo"
human = Animal("hey")
pet = Dog("Dot")
Cat = Cat("claw")
print(human.name ,pet.name, Cat.name)
print(human.talk(), pet.talk(),Cat.talk())
