
# main_number = 15
# user_input = 0
# while user_input != main_number:
#     user_input = input("Guess a number 0 - 20: ")
#     user_input = int(user_input)
#     print (type(user_input))
#     print(f"You entered {user_input} number")
#     print(user_input != main_number)
# print ("Done")

main_number = 15
while True:
    user_input = input("Guess a number 0 - 20: ")
    print(f"You entered {user_input} number")
    if int(user_input) == main_number:
        break   #exits the loop
    else:
        continue
print ("Done")

capitals = {"Argentina": "Buenos Aires", "Armenia": "Yerevan", "Australia": "Canberra", "Austria": "Vienna"}

user_input = "armenia"
#

for country, capital in capitals.items():
    print("current country: " + country)
    if user_input.lower() == country.lower():
        print("Capital is: " + capital)
        break


book_prices = {"calculus": 300, "physics": 255, "chemistry": 400, "english": 150, "theater": 160}
my_courses = ["physics", "english", "psycology", "calculus", "history"]
total_cost = 0
for cource in my_courses:
    if cource not in book_prices.keys():
        continue
    total_cost += book_prices[cource]
    total_cost = total_cost + book_prices[cource]

print("Total books cost: {}".format(total_cost))