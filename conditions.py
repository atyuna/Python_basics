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
