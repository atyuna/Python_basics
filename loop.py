# for loop

colors = ["blue", "green", "red", "orange", "yellow"]


for color in colors:
    print("Do you like {} color ?".format(color))


for number in range(1,11):
    print("Number {}".format(number))

    
 # while loop

temp_f = 40

while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
# Loop control statements: break, continue, pass
    if temp_f == 33:
        break
        
for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))
    

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}.".format(number))
        
        
#______________


# need to kill this endless loop:
# while True:
#     print("abc")

# counter  = 1
# while True:
#     print(counter)

# good loop:
counter = 1
while counter <= 10:
    print(counter)
    counter = counter + 1
