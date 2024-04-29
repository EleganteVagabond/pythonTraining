def say_hello():
    '''This is a docstring '''
    print("hello")

# The starter code for the program built in the video below:
# print("Welcome to the program, what is your name?")
# name_result = input("Enter your response here -> ")
# print(f"Your response was {name_result}")
#
# print("What did you think of the food you ate today?")
# food_result = input("Enter your response here -> ")
# print(f"Your response was {food_result}")
#
# print("What tv show ending did you dislike the most ever?")
# show_result = input("Enter your response here -> ")
# print(f"Your response was {show_result}")

def get_and_print_input(prompt):
    print(prompt)
    result = input("Enter your respone here -> ")
    print(f"Your response was {result}")

# use functions
# get_and_print_input("Welcome to the program, what is your name?")
#
# get_and_print_input("What did you think of the food you ate today?")
#
# get_and_print_input("What tv show ending did you dislike the most ever?")


def get_and_print_all_input(prompts):
    results = dict()
    for k,prompt in prompts.items():
        print(prompt)
        results[k] = input("Enter your response here -> ")
    for k,v in results.items():
        print(f"To the question about {k} you responded with:\t'{v}'")

get_and_print_all_input({"Name":"What is your name","Food" : "What is your food","TV":"What is your TV"})
