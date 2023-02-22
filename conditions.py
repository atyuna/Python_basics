shows = ["Uno", "Doom", "little F"]
movies = ["Marina", "Lara Croft", "The huntress"]

my_choise = 'Uno'

if (my_choise in movies) or (my_choise in shows):
    print("Your choise is valid")
else:
    print("Your choise is unknown")


if my_choise in movies:
    print("Your choise is a movie")
elif my_choise in shows:
    print("Your choise is a show")
else:
    print("Your choise is not valid")

    
#--------- Nested if - else


theater = "Lumbaba"
rated_r_age_limit = 17

print(f"Welcome to {theater} !!!")

user_input = input("Enter your age: ")
print(f"User input is {user_input}.")

if int(user_input) >= rated_r_age_limit:
    print("Enjoy the movie")
else:
    adult_present = input("Is the adult with you present? Yes or No? :")
    if adult_present.lower() == "yes":
        print("Enjoy the movie!")
    else:
        print("Sorry, You must be 17 to watch the movie")
