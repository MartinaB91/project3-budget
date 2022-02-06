import utils

def save_new_user_to_worksheet(): 
    """ Reads user inputs, give the user a unique id and save user 
    input in list and later appends list to worksheet. """
    user_fname = input("Enter your firstname: \n")
    user_lname = input("Enter your lastname: \n")
    username = input("Enter your username: \n")
    new_user_id = utils.give_data_id('users')
    user = [new_user_id, username, user_fname, user_lname]
    utils.save_data_to_worksheet('users', user) 
    return username

def get_active_user():
    """ Prints user menu options and let the user enter a username. 
    Depending on user selection the function return active user(old or new user)."""
    menu_options = ("Welcome to your budget program \n1. Enter your username. \n2. Create a new user.")
    print(menu_options)
    selected_option = input("Please select a menu option (1-2): \n")

    if selected_option == "1":
        active_user = input("Enter your username: \n")
        return active_user
    elif selected_option == "2":
        active_user = save_new_user_to_worksheet()
        return active_user
    else: # Used when no valid menu option is selected. Call function to let user try again. 
        print(f"{selected_option} is not a valid menu option. Please try again.")
        get_active_user()

