import random

class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20
    def attack(self,other_guy):

        other_guy.health = other_guy.health - self.damage
        print("{} attacks {}!".format(self.name, other_guy.name))
        print("{} loses {} health points!".format(other_guy.name, self.damage))
        print("{} health reduced to {}".format(other_guy.name, other_guy.health))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)
class Evolved(Fighter):
    def Critical(self):
        self.damage += random.randint(1,20)
    def Regeneration(self):
        self.health += 10

Evolved_Tony = Evolved("TonyKai")
# Tony = Fighter("Tony")
Qazi = Fighter("Qazi")
#
# Tony.attack(Qazi)
Evolved_Tony.Regeneration()
Evolved_Tony.Critical()
Evolved_Tony.attack(Qazi)
print(Qazi,Evolved_Tony.health)

# print(Qazi)
