# hello_you

# Function to get the name input so I can reuse it for different exercises
def get_name_input(): 
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    return name

# Only run get_name_input() if this file is being run directly and not imported.
if __name__ == "__main__":
    get_name_input()