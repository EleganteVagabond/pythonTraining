def get_input_from_user(my_list):
    my_list.append(input("type"))

l = []
num_loops = 3
for i in range(num_loops):
    get_input_from_user(l)
    print(l)
