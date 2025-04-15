import random
guess_prompt = "I am thinking of a number between 1 and 10."

secret_num = random.randint(1, 10)
print(guess_prompt)

guesses = 5

while guesses > 0 :
    guess_num = int(input(" What's the number? "))
    
    if guess_num == secret_num :
        print("Yes! You win!")
        break
    elif guess_num < secret_num :
        print(f"{guess_num} is too low.")
    else :
        print(f"{guess_num} is too high.")
    
    guesses -= 1
    
    if guesses == 0 :
        print("You are out of guesses!")
    else :
        print(f"You have {guesses} guesses left.")