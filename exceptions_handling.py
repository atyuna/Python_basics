
# simple try-catch:

try:
    a = 5/0
except:
    print("Don't divide by 0! ")

# catch specific error:
try:
    a = 5/0
except ZeroDivisionError:
    print("ZeroDivisionError catch! ")

# catch and print the actual error:
try:
    a = 5/0
except ZeroDivisionError as e:
    print(f"Error has happened: {e}!")

# catch any type of error:
try:
    a = "abc"/0
    # print(foo)     # NameError
except Exception as e:
    print(f"Error has happened: {e}!")

# catch multiple exceptions in one block:
try:
    #a = "abc"/0
    b = {"name": "Anya", "school": "123"}
    c = b["age"]        # KeyError
except (KeyError, ZeroDivisionError) as e:    # few errors handling in a tuple
    print(f"Error has happened!")

# catch multiple exceptions in multiple blocks:
try:
    #a = "abc"/0
    b = {"name": "Anya", "school": "123"}
    c = b["age"]        # KeyError
except KeyError as e:
    print('Key issue')
except ZeroDivisionError:
    print("Division by zero issue")

# Example raise an exception:

raise Exception ("Errorrrrr")
