# create class

class Human:
    def __init__(self, firstname, lastname, health, status, sex):
        " initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class."
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
        self.sex = sex



    def introduce(self):
        "All humans introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def status_change(self):    #loop for changing health status
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Human("Maria", "Hines", 95, status=True, sex = "female")
Joe = Human("Joe", "Jones", 88, status=False, sex = "men")
Qui = Human("Qui", "Lin", 72, status=True, sex = "female")

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is {}".format(Maria.firstname, Maria.sex))

print("{} is my friend? {}".format(Joe.firstname, Joe.status))
print("{} is {}".format(Joe.firstname, Joe.sex))

#   Inheritance, Multiple Inheritance, Polymorphism

class Enemy(Human):
    def __init__(self, weapon, firstname, lastname, health, status, sex):
        super().__init__(firstname, lastname, health, status, sex)
        self.weapon = weapon

    # example of polymorphism :
    def introduce(self):
        print("You are my mortal enemy!!!")

    # 3 methods of Enemy class:

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -=5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy("rock", "Alex", "Wayne", 75, status = False, sex = "male")
Alex.hurt(Maria)
Alex.insult(Qui)
Alex.steal(Joe)

# Joe.steal(Alex) - will not work, because Human class doesn't have steal() method

#    Polymorphism   - when child can owerride the method of the parent
Alex.introduce()
