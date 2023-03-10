
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

class Dog(Animal):

    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.dog_breed = breed
        self.dog_name = name

    def bark(self):
        print("WOOOF")

    def as_security(self):
        print("My dog is my home security")


class Cat(Animal):

    def __init__(self,color, food_type, breed, name):
        super().__init__(color, food_type)
        self.cat_breed = breed
        self.cat_name = name

    def meow(self):
        print('meowwww.....')

myDog = Dog('black','meat','bulldog','Jim')
print(myDog.dog_breed, myDog.dog_name)
myDog.eat()

myCat = Cat('white', 'cats food', 'Brit', 'Lord')
myCat.eat()
myCat.meow()
