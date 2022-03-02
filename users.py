import utils

def save_new_user_to_worksheet(): 
    """ Reads user inputs, give the user a unique id and save user 
    input to worksheet. """     
    user_fname = utils.get_input_only_letters("Enter your firstname:\n", "Your firstname can only contain letters, please try again!\n")
    user_lname = utils.get_input_only_letters("Enter your lastname:\n", "Your lastname can only contain letters, please try again!\n" )
    username = input("Enter your username: \n")
    new_user_id = utils.give_data_id('users')
    user = [new_user_id, username, user_fname, user_lname] # saves data in a list
    utils.save_data_to_worksheet('users', user) 
    return user

def get_active_user():
    """ Prints user menu options and let the user enter a username. 
    Depending on user selection the function return active user(old or new user)."""
    menu_options = ("Welcome to your budget program \n1. Enter your username. \n2. Create a new user.")
    print(menu_options)
    selected_option = input("Please select a menu option (1-2): \n")

    if selected_option == "1":
        username_input = input("Enter your username: \n") # Todo: Find id of user.
        users = utils.get_all_info_from_worksheet('users')

        """Search in all saved user in sheet to find if entered name is a user. Inspiration from:
        https://stackoverflow.com/questions/14790980/how-can-i-check-if-key-exists-in-list-of-dicts-in-python"""
        active_user = [dict for dict in users if dict["username"] == username_input]
        if any(active_user): 
            print(f"Hi, {username_input} good to have you back!")
            return active_user
        else:
            print(f"The username you have entered, {username_input} doesn't exist. Please try again")
            get_active_user()

    elif selected_option == "2":
        active_user = save_new_user_to_worksheet()
        return active_user
    else: # Used when no valid menu option is selected. Call function to let user try again. 
        print(f"{selected_option} is not a valid menu option. Please try again.")
        get_active_user()


