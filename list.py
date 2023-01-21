
city_name = ["Mosk", "Berlin", "Kyiv"]
crimes: list[int] = [30000, 20500, 200]
population = [10000, 2040, 25]
norm_crimes = [3000.0, 10049.019607843136, 8000.0]

print(city_name, crimes, population)

# methods to add to the list: .append, .extend

city_name.append("Cary")
print(city_name, crimes, population)

city_name.extend(crimes)
print(city_name, crimes)
