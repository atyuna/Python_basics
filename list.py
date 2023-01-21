
city_name = ["Mosk", "Berlin", "Kyiv"]
crimes: list[int] = [30000, 20500, 200]
population = [10000, 2040, 25]
norm_crimes = [3000.0, 10049.019607843136, 8000.0]

print(city_name, crimes, population)

# methods to add to the list: .append(), .extend()

city_name.append("Cary")
print(city_name, crimes, population)

city_name.extend(crimes)
print(city_name, crimes)


# methods to remove from the list: .remove(), .pop()
city_name.remove("Mosk") #removes by name
print (city_name)

city_name.pop(0) #removes by the index
print (city_name)

city_name.pop(-2) #removes by the index from the end
print (city_name)


#.sort() method (can sort only items of like data types in list)
num = [99, 209, 23, 9.5, 4, 0, 2933]
num.sort()
print(num)


# in keyword used to check if the item is in the list

print("Bora" in city_name) # - False, there is no such item in the list

# count() method returns the number of times the specified element appears in the list.

apples = ["Alma", "Grenny", "Mariani", "Golden", "Alma", "Golden"]
print(apples.count("Alma"))
print(apples.index("Mariani"))  #index() searches the position of the item in the list
