
class Dinosaur:

    def __init__(self):
        self.name = 'Shelbasauraus'
        self.health = 100
        self.attack_power = 25
        

    def attack(self, robot):
        robot.health -= self.attack_power
        print ('Shelbasauraus headbutts Rebelbot for a damage of 25!')
        
