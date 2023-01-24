#create class

class House:
    # house description
    def __init__(self, street, number):
        # house properties
        self.street = street
        self.number = number

    def build(self):
        # build a house
        print("House on the street " + self.street + " with number "+ str(self.number) + " has built")

House1 = House("Faulkner", 120)
House2 = House("Faulkner", 121)

print(House1.street)
print(House2.number)

House1.build()

class AvenueHouse(House):
    # child of House class (subclass)
    def __init__(self, avenue, number):
        super().__init__(self, number)  # for inheritance
        self.avenue = avenue

AvHouse = AvenueHouse("Hopson", 23)
print(AvHouse.number)
