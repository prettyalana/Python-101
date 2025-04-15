# Coins
coins = int(0)

print (f"You have {coins} coins.")

add_coin = input(f"Do you want another? ")

# If I want the loop to end 
STOP = 10

# This is an infinite loop
while coins == coins:
    if add_coin == "yes" :
        coins += 1
        print(f"You have {coins} coins")
        add_coin = input(f"Do you want another? ")
    else :
        print("Bye")
        exit()