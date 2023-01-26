def create_story (name, age, job):      # (name, age, job) - parameters
    print (f"{name} is {age} and she worked as a {job}.")

create_story("Lisa", 32, "cook")        # ("Lisa", 32, "cook") - positional arguments

def create_story2 (name, age = 23, job= "Programmer"):  #added default values
    print (f"{name} is {age} and he worked as a {job}.")

create_story2("Jim")
create_story2("Alex", age=43)   # age=43 - keyword args
create_story2("Milko", job="teacher")   # job="teacher" - keyword args


def create_story3 (name, age = 45, job= "composer", *args, **kwargs):  # *args- should handle any number of positional args;  **kwargs - should be able to handle any number of keyword arguments
    print (f"{name} is {age} and she worked as a {job}.")

create_story3("Zila", job="CEO", kids=2, email = "zila@gmail.com")
