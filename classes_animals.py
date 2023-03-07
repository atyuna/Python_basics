
import pdb

class Animal:
    def __init__(self, color,food_type):
        print("I'm init")
        self.color = color
        self.food_type = food_type

    def move(self):
        print("Animal moves")

    def eat(self):
        print("Animal eat")
        print("This animal eats {}".format(self.food_type))

    def breath(self):
        print("Animal breaths")

my_animal1 = Animal('blue','grass')
print(f'Color of animal 1 is {my_animal1.color}')
my_animal1.move()
my_animal1.eat()


my_animal2 = Animal('red','meat')
print(f'Color of animal 2 is {my_animal2.color}')
