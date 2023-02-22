new_dict = {}
type(new_dict)

income = {'Laslo': 123000, 'Anya': 1000, 'Dilan':[2345,3400,5730]}

income.update({'Vova': [5253, 57685, 8929329]}) # updates the dictionary
print(income.get("Laslo"))  # returns the value 
print(income.keys())  # returns all keys
income.popitem()  # removes the last item added({'Vova': [5253, 57685, 8929329]})
income.setdefault("John", 23120)  # adds default value and key
print(income)

income.update({"Boris": 234123})    #updates the dictionary
new_income = {"Mila": 4324}
income.update(new_income)
print(income)


# __________________________

capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
print(type(capitals))

# getting items from dictionary

france_capital = capitals["France"]
print(france_capital)
france_capital2 = capitals.get("France")
print(france_capital2)

# get key that does not exist
#egypt_capital = capitals["Egypt"]  will fail
egypt_capital2 = capitals.get("Egypt","NO DATA")
print(egypt_capital2)


# Adding item to dictionary
# Option 1
print(capitals)
print("option 1 for adding data into dictionary: ")
capitals["Kenya"] = "Nairobi"
print(capitals)

# Option 2
print("option 2 for adding data into dictionary: ")
capitals.update({"India":"New Dehli"})
print(capitals)

print("============")
print(capitals)
all_keys = capitals.keys()
all_values = capitals.values()
print(all_keys)
print(all_values)


employee = {"name":"Jon Doe",
            "title":"Sr. test engineer",
            "age": 34,
            "phone": 91923485319,
            "skills":["AWS", "Python", "Java", "Doker"]
}
e_name = employee['name']
e_skills = employee['skills']
e_title = employee['title']
e_phone = employee['phone']
print(type(e_skills))
user_skills = len(e_skills)
print(f"{e_name} has {user_skills} skills")
