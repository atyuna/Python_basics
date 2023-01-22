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
