#Import the get_name_input function from hello_you 
from hello_you import get_name_input

# Madlib
prompt = "Please fill in the blanks below:"
name = get_name_input()
user_name = name.capitalize()
fav_subject = input("What is your favorite subject? ")
print(prompt)
print(f"{user_name}'s favorite subject in school is {fav_subject}.")