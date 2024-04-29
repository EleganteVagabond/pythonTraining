l=[6,8,1,4,10,7,8,9,3,2,5]
sum = 0
for val in l:
    sum += val

print(sum)

# range creates a defacto list
print(list(range(10)))
print(list(range(1,10,2)))
sum2 = 0
for val in range(len(l)) :
    sum2 += val
print(sum2)

#dictionaries
my_dict={'py':'python','rb':'ruby','js':'javascript'}
for item in my_dict:
    print(item)

for item in my_dict.items():
    # tuple
    k,v=item
    print(k,v)

#gen nums
from random import randint
l1 = []
for i in range(100):
    l1.append(randint(1,100))
print(l1)

# shorthand for above
l2 =[randint(1,100) for num in range(100)]
print(l2)

from string import ascii_lowercase
from random import choice
# can do many things with this notation, in this case choose any of the items in the ascii_lowercase list
l3 =[choice(ascii_lowercase) for num in range(100)]
print(l3)
