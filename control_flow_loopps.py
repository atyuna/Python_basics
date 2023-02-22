
for i in range(9):
    print(i)

print("--------------")

for i in range(5,12):
    print(i)

print("--------------")

names = []
for i in range(4):
    names.append("ABC")
print(names)
print(len(names))


#_____________


cars = ["BMW", "Honda", "Toyota"]

for car in cars:
    print(car)
    print("_______")


quote = "How can I make an interesting app?"
for i in quote:
    print(i)

# convert to the list
# print words with >= 3 caracters
#   words_list = quote.split()
#   print(words_list)
#   for i in words_list:
for i in quote.split():
    if len(i) <= 3:
        print(i)

# collect all small words into the list and print the list

quote1 = "I learn to code with Python"
small_words = []
for i in quote1.split():
    if len(i) <= 3:
        small_words.append(i)
print(small_words)

loplist = []
for i in loplist:
    print("a")
    
    
    #____________
    
    
