import random

class Fighter:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return "{}: health {}".format(self.name, self.health)

    def attack(self):
        self.damage = random.randint(1,20)
        
    def update_health(self,other_guy):
        self.health = self.health - other_guy.damage
        return f'{self.name} health is {self.health}'

Gus = Fighter("Gus")
Joey = Fighter("Joey")

player_list = [Gus,Joey]
 user = str(input('continue?[yes/no]'))
    if user == 'no':
        break
while True:
    for player in player_list:
        player.attack()
        if player.health < 0:
            player_list.remove(player)
    
    user = str(input('continue?[yes/no]'))
    if user == 'no':
        break
            

    if len(player_list) == 1:
        print(f'{player_list[0]} has won!')
        break
        
                
    player_list[0].update_health(player_list[1])
    player_list[1].update_health(player_list[0])
    print("Gus takes " + str(Joey.damage) + " points of damage!")
    print("Gus has "  + str(Gus.health) + " health points left!")
    print("Joey takes " + str(Gus.damage) + " points of damage!")
    print("Gus has "  + str(Joey.health) + " health points left!")
  
