## Function frames and variable scope
# Below is the initial implementation
def func_0(start_num):
    start_num += 1
    return func_1(start_num)

def func_1(start_num):
    start_num += 1
    return start_num

start_num = 1
print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t-> {finish_num}")
print(f"start_num\t-> {start_num}")
print(finish_num == start_num)

# Below is the implementation using a list
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

# Execution code below using same list object
start_num = [1]
print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t-> {finish_num}")
print(f"start_num\t-> {start_num}")
print(finish_num == start_num)

# Execution code below using a copied list
start_num = [1]
print(f"start_num\t-> {start_num}")
finish_num = func_0(start_num[:])
print(f"calc'd_num\t-> {finish_num}")
print(f"start_num\t-> {start_num}")
print(finish_num == start_num)
