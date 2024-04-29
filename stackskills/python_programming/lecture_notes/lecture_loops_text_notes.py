# For loops for iterating through iterables

# For the list defined below, we explored two ways of iterating
# through the list and calculating the sum of all elements in it
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

sum = 0
for num in l:
    sum += num
print(f"Sum using list: {sum}")

# Same calculation done using range generator, which gives us an iterable
sum = 0
for num in range(len(l)):
    sum += l[num]
print(f"Sum using range generator: {sum}")

# Range is very useful if you don't know ahead of time how many times
# you want an iteration in a for loop to take place, example below
# with an input received from the user
run_times = int(input("How many times do you want the program to run? "))
for num in range(run_times):
    print(f"Run: {num+1}")

# You can generate a list of random integers using the range function
# in combination with the randint function from the random module
from random import randint
l1 = []
for num in range(25):
    l1.append(randint(1, 100))
print(l1)
print(len(l1)) # Checking the number of integers generated

# You can do the same using list comprehension in 1 line below
l1 = [randint(1,100) for num in range(25)]
print(l1)
print(len(l1)) # Checking the number of integers generated

# You can use the items method to get an iterable from a dictionary
# then you can iterate through the tuples of key value pairs that
# this provides to print them out, or use them in other ways

my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}
for k, v in my_dict.items():
    print(f"Extension of .{k} means it's a {v} program")
