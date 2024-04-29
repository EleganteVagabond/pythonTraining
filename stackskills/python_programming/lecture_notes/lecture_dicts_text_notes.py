## Dictionaries
# Dictionaries are key value pairs and look like below:
my_dictionary = {'name': 'mashrur', 'course': 'python', 'fav_food': 'ice cream'}
phone_dict = {'mashrur': '555-55-5555',
              'zoolander': '999-99-9999',
              'jon_snow': 'fail-o-so-bad'}
word_dict = {'a':
                {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor'
                },
             'b':
                {
                 'bad': 'of poor quaity or low standard',
                 'business': 'season 8 of GOT'
                }
            }
print(my_dictionary)
print(phone_dict)
print(word_dict)

# Dictionary keys should be immutable data types like strings and integers
# To access a value, provide the key, for example if I wanted
# the value associated with 'name' in my_dictionary above, I'd do
# the following
print(my_dictionary['name'])

# I can re-assign the value associated with a key by using the key
my_dictionary['name'] = 'john'
print(my_dictionary)

# I can add in a key value pair that doesn't exist in the dictionary
my_dictionary['job'] = 'python programmer'
print(my_dictionary)

# I can keep going deeper by providing the keys one after the other
# To access the value of business in the word_dict above, I can do
# the following
print(word_dict['b']['business'])

# Use some methods to get keys, values and key, value pair as iterable
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

# Get a listing of some methods available to dictionaries to test
# them out by using the dir function
print(dir(my_dictionary))

# You can iterate through the key value pairs using a for loop
for key, value in my_dictionary.items():
    print(f'Key: {key}, Value: {value}')
