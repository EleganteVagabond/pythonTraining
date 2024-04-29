## Sets are un-ordered collections of data with no duplicates

my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python'}
print(my_set)

# If you have a list with duplicates, you can cast it to a set
# to get rid of duplicates fast
my_list = [1,6,2,'java','ruby',8,9,10,21,1000,6,'python','java']
print(my_list)
my_set = set(my_list)
print(my_set)

# You can find information in sets using 'in'
print('java' in my_set)

# Examples of methods available to sets below
# you can explore others by using dir(my_set)
my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python'}
programming_set = {'java','ruby','javascript','python','c'}
print(my_set.intersection(programming_set)) # elements in common in both sets
print(my_set.union(programming_set)) # all elements in both, no duplicates
print(my_set.difference(programming_set)) # in my_set, not in other
print(programming_set.difference(my_set)) # in programming_set, not in my_set

# You can iterate through items in a set using a simple for loop
for item in my_set:
    print(item)
