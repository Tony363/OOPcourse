# class Fighter:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.damange = 20
#     def attack(self,other_guy):
#
#         other_guy.health = other_guy.health - self.damange
#         print("{} attacks {}!".format(self.name, other_guy.name))
#         print("{} loses {} health points!".format(other_guy.name, self.damange))
#         print("{} health reduced to {}".format(other_guy.name, other_guy.health))
#
#     def __str__(self):
#         return "{}: {}".format(self.name, self.health)
#
# Tony = Fighter("Tony")
# Qazi = Fighter("Qazi")
#
# Tony.attack(Qazi)
#
# print(Qazi)
#
# class Fighter:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.damage = 10
#     def attack(self, other_guy):
#         other_guy.health = other_guy.health - self.damage
#
# qazi = Fighter("Qazi")
# you = Fighter("Matt")
# print(qazi.name, you.name)
# you.attack(qazi)
# print(qazi.health)
import random

class Fighter:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = random.randint(1,20)
        # self.current_health = self.health - self.damage

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print("{} attacks {}".format(self.name, other_guy.name))
    def __str__(self):
        return "{}: {}".format(self.name, self.health)

Gus = Fighter("Gus")
Joey = Fighter("Joey")

print(Gus)
print(Joey)

Joey.attack(Gus)
print("Gus takes " + str(Joey.damage) + " points of damage!")

print("Gus has "  + str(Gus.health) + " health points left!")
