
def start_program():
    # Present user with options over what choises they have and what they can do in this program.
    print("Welcome to your budget program")
    print("What do you want to do?")
    print("1. Create a new budget")
    print("2. Add purchase to ongoing budget")
    print("3. Get a summary of budget")
    print("4. End ongoing budget")

    user_want_to = input("Please enter the number of your chooise: \n")
    # Depending on what choice the user choose it will lead to different "pages". Every page has its a own function.
    if user_want_to == 1:
        print(user_want_to)
    elif user_want_to == 2:
        print(user_want_to)
    elif user_want_to == 3:
        print(user_want_to)
    elif user_want_to == 4:
        print(user_want_to)
    elif user_want_to == 5:
        print(user_want_to)
  
start_program()
