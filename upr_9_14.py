from random import randint
#x = randint(1,6)
#print(x)

class Die():
    def __init__(self, sides = 6):
        self.sides = randint(1,sides)
    def roll_die(self):
        print(self.sides)

kub = Die(20)
kub.roll_die()
