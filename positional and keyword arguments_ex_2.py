
# examples of using keyword parameters
#1 write a func that will return a number of words that have X length

def get_count_of_small_words (input_string, max_size = 3):

    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)

    return len(small_words)

joke = "Why do Python developers prefer Macs? Because they don't like snakes on their Windows!"

#num_small = get_count_of_small_words(joke)
num_small = get_count_of_small_words(joke, 5)
print(num_small)


# Example 2:

def connect_to_database(host = 'test.db.com', username = 'testqa', password = 'qwe123'):
    print(f"Connecting to host {host}")
    print(f'Username is {username}')

connect_to_database()
connect_to_database(host='prod.db.com', username='prodqa', password='123')
# the same:
connect_to_database('prod.db.com', 'prodqa', '123')
