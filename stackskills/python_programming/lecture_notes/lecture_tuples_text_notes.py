## Tuples
# Key thing to remember about tuples is they are immutable

my_random_tuple = ('first',1,7,6,4,5,8,'hi there',2,3,1,5,2,1,9,10)
my_tuple = ('first_value','second_value','third_value')

print(my_random_tuple)
print(my_tuple)

# You can 'unpack' the elements in a tuple by using tuple unpacking
first_var, second_var, third_var = my_tuple
print(first_var, second_var, third_var)

# You can find out if an item exists in your tuple using 'in'
print('hi there' in my_random_tuple)

# You can use index and slice notation on tuples
print(my_random_tuple[7])
print(my_random_tuple[7:])

# You can iterate through the items in a tuple using a simple for loop
for item in my_random_tuple:
    print(item)
    
# Try running the index and count methods on the tuples above
# along with the len function
