from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon
        print (f'{name} is your robots name and has a weapon of {Weapon(name)}.')
        

    def attack(self,dinosaur):
        pass

