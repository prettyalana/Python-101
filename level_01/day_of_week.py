# Day of the Week
def day_input():
    day = int(input('Day (0-6)? '))
    return day

# Only run this if I run this file directly; prevent it from running in imports
if __name__ == "__main__":
    
    day = day_input()

    if day == 0 :
        print("Sunday")
    elif day == 1 :
        print ("Monday")
    elif day == 2 :
        print ("Tuesday")
    elif day == 3 :
        print ("Wednesday")
    elif day == 4 :
        print ("Thursday")
    elif day == 5 :
        print ("Friday")
    else :
        print ("Saturday")