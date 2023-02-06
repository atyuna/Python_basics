# Inheritance from multiple classes - the order matters!
# 2 ways for multiple inheritance

# create Parent class 1
class Item():
    def __init__(self,sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}".format(self.sku))

# create Parent class2  - child uses and access atributes and methods of the parent classes
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))

Blouse = Shirts("0006", 43, "Tops", "Formal Blouse", "white")

Blouse.print_sku() #  method of Parent 1
Blouse.print_garment()  #  method of Parent 2
Blouse.print_shirt()        #  method of Child



