from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = 'Rebelbot'
        self.health = 100
        self.active_weapon = Weapon('ax', 20)
        
        print ('Rebelbot uses his ax and does damage of 20!')
        

    def attack(self,dinosaur):
        dinosaur = -self.active_weapon.attack_power
        print(dinosaur)


