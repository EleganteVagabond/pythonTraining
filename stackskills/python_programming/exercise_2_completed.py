import random

# Question 1: Use list comprehension to update the code below and
# assign my_list to be a list of 200 random integers ranging in values
# between 25 and 500. Hint: Use the randint function
my_list = [random.randint(25,500) for i in range(200)] # replace the code to the left

# Question 2 (4 parts): Cast my_list to a set and re-assign to my_list as a list.
# How many duplicate values were removed?
initial_size = len(my_list) # replace the code to the left
print(f"Initial size of my_list: {initial_size}")
# cast the list to a set to remove duplicates and re-assign to my_list as a list
my_set = set(my_list) # replace the code to the left
final_size = len(my_set) # replace the code to the left
print(f"Final size of my_list after removing duplicates: {final_size}")
dups_removed = initial_size-final_size # replace the code to the left
print(f"Number of integers removed: {dups_removed}")
print('-'*40)
print()

# Question 3: What is the largest integer in my_list?
largest_val = max(my_list) # replace the code to the left
print(f"Largest integer in my_list: {largest_val}")
print('-'*40)
print()

# Question 4: What is the smallest value in my_list?
smallest_val = min(my_list) # replace the code to the left
print(f"Smallest integer in my_list: {smallest_val}")
print('-'*40)
print()

# Question 5: Create a tuple with the exact same values as my_list
# name it my_tuple
my_tuple = tuple(num for num in my_list) # replace the code to the left

# Question 6: What are the last 3 values of my_tuple?
my_tuple_last_val = my_tuple[-1] # replace the code to the left
my_tuple_sec_last_val = my_tuple[-2] # replace the code to the left
my_tuple_third_last_val = my_tuple[-3] # replace the code to the left
print(f"The last 3 values of the tuple are {(my_tuple_third_last_val,my_tuple_sec_last_val,my_tuple_last_val)}")
print('-'*40)
print()

# Question 7: Create a new tuple with all the values of my_tuple in
# reversed order
my_new_tuple = tuple(num for num in my_tuple[::-1]) # replace the code to the left

# Question 8: Does the first value of my_new_tuple match my_tuple_last_val?
# Enter in the conditional below that will evaluate to True or False
comparison = my_new_tuple[0]==my_tuple[-1] # replace the code to the left
print(f"First integer of my_tuple matches last integer of my_new_tuple is a {comparison} statement")
print('-'*40)
print()

# Question 9: Create a new tuple with the first 5 values of my_new_tuple
my_other_tuple = tuple(num for num in my_new_tuple[:5]) # replace the code to the left
print(f"My newly created 5 integer tuple is {my_other_tuple}")
print('-'*40)
print()

# Question 10: Do the integers (ignore order) of my_other_tuple match the values of
# the last 5 integers in my_list? replace the boolean below with
# a conditional that evaluates to True or False. You can use other variables
# below as you need to complete this.
tuple_and_list_comp = len(set(my_other_tuple).difference(my_list[-6:]))==0 # replace the code to the left
print(f"Integers in my_other_tuple match the last 5 integers of my_list is a {tuple_and_list_comp} statement")
print('-'*40)
print()

# Question 11: Find the intersection between the following two sets and
# store it in my_match
my_requirements = {'ruby','python'}
available_languages = {"comp sci", "physics", "elec engr", "philosophy", "python"}
my_match = my_requirements.intersection(available_languages) # replace the code to the left
print(f"I can take {my_match} since I need it and it's available")
print('-'*40)
print()

# Question 12: Given the dictionary below, create a list called my_al_list
# which includes only the values (meaning) associated with each word.
# my_al_list should look like ['the round fruit of a tree of the rose family',
# 'an insect which cleans up the floor'......].
# Obviously do this programmatically and don't hardcode it, you may use
# other lines of code and variables as you see fit. Solution code has a couple of
# options displayed.

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

my_al_list = [] # replace the code to the left
for k,v in word_dict.items():
    my_al_list.extend( [wv for wk,wv in v.items()])
print(f"The meanings in the dictionary are {my_al_list}")

# Option 2, list comprehension
my_al_list = [list(v.values()) for v in word_dict.values()]
print(my_al_list)
# Flatten to remove list of lists and convert to a single list
my_al_list = [v for dets in my_al_list for v in dets]
print(f"The meanings in the dictionary are {my_al_list}")

# Option 3 (advanced), use itertools chain + list comprehension combo
from itertools import chain
#my_al_list = list(chain.from_iterable([list(combo.values()) for index, combo in word_dict.items()]))
my_al_list = list(chain.from_iterable([list(vs.values()) for vs in word_dict.values()]))
print(f"The meanings in the dictionary are {my_al_list}")
