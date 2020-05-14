## Functions

# The starter code for the program built in the video below:
print("Welcome to the program, what is your name?")
name_result = input("Enter your response here -> ")
print(f"Your response was {name_result}")

print("What did you think of the food you ate today?")
food_result = input("Enter your response here -> ")
print(f"Your response was {food_result}")

print("What tv show ending did you dislike the most ever?")
show_result = input("Enter your response here -> ")
print(f"Your response was {show_result}")


# The final code for the function at the end of the video below:
def get_input_from_user():
    return input("Enter your response here -> ")

print("Welcome to the program, what is your name?")
name_result = get_input_from_user()

print("What did you think of the food you ate today?")
food_result = get_input_from_user()

print("What tv show ending did you dislike the most ever?")
show_result = get_input_from_user()

print(f"To summarize: Your name is {name_result.capitalize()},\
 you ate {food_result} food today and hated the ending\
 of {show_result.upper()}")
