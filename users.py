from emoji import emojize
import utils
import colors


def save_new_user_to_worksheet():
    """Reads user inputs, give the user a unique id and save user
    input to worksheet."""
    user_fname = utils.get_input_only_letters(
        (f"{colors.Colors.pink}Enter your firstname:{colors.Colors.white}\n"),
        "Your firstname can only contain letters, please try again!\n",
    )
    user_lname = utils.get_input_only_letters(
        (f"{colors.Colors.pink}Enter your lastname:{colors.Colors.white}\n"),
        "Your lastname can only contain letters, please try again!\n",
    )
    users = utils.get_all_info_from_worksheet("users")
    try_again = True
    while try_again == True:  # As long as user select a taken username the system ask user for another username.
        username = input(f"{colors.Colors.pink}Enter your username:{colors.Colors.white} \n")

        """ Inspiration from: https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/
        and https://stackoverflow.com/questions/2405292/check-if-string-contains-only-whitespace
        """
        if len(username) != 0 and username.isspace() is False: 
            user_class_list = [dict for dict in users if dict["username"] == username]
            if len(user_class_list) == 0:  # If list contains no user, username is not taken.
                try_again = False
            else:
                colors.print_text_color_red('This username is already taken, please try another username!')
        else:  #  If username is empty or only blank spaces print this. 
            colors.print_text_color_red("Your username can't be empty")
   
    new_user_id = utils.give_data_id("users")
    # saves data in a list
    user = [new_user_id, username, user_fname, user_lname]
    utils.save_data_to_worksheet("users", user)
    return user


def get_active_user():
    """Prints user menu options and let the user enter a username.
    Depending on user selection the function return active user(old or new user)."""
    #  Emojis. Inspiration from: https://unicode.org/emoji/charts/full-emoji-list.html and https://www.codegrepper.com/code-examples/python/import+emoji+in+python
    colors.print_text_color_green(emojize(":money_bag: " + ":euro_banknote: " + "Welcome to your budget program" + " :money_bag:" + " :euro_banknote:\n"))
    menu_options = "1. Enter your username. \n2. Create a new user.\n"
    colors.print_text_color_blue(menu_options)
    selected_option = input("Please select a menu option (1-2): \n")

    if selected_option == "1":
        username_input = input(f"{colors.Colors.pink}Enter your username:{colors.Colors.white} \n")
        users = utils.get_all_info_from_worksheet("users")

        """Search in all saved user in sheet to find if entered name is a user. 
        Inspiration from: https://stackoverflow.com/questions/14790980/how-can-i-check-if-key-exists-in-list-of-dicts-in-python"""
        active_user_class_list = [dict for dict in users if dict["username"] == username_input]
      
        if len(active_user_class_list) != 0:  #  If the list contain a user do this.
            #  Save data to dictionary.
            active_user = {
                'id': active_user_class_list[0]['id'],
                'username': active_user_class_list[0]['username'],
                'first_name': active_user_class_list[0]['first_name'],
                'last_name': active_user_class_list[0]['last_name']
            }
            colors.print_text_color_purple(emojize(f"Hi, {username_input} good to have you back!" + ":slightly_smiling_face:\n"))
            return active_user
        else:
            colors.print_text_color_red(
                f"The username you have entered, {username_input} doesn't exist. Please try again"
            )
            return get_active_user()

    elif selected_option == "2":
        colors.print_text_color_purple("Let's create a new user!\n")
        active_user_class_list = save_new_user_to_worksheet()
        #  Save data to dictionary.
        active_user = {
            'id': active_user_class_list[0],
            'username': active_user_class_list[1],
            'first_name': active_user_class_list[2],
            'last_name': active_user_class_list[3]
        }
        colors.print_text_color_green(f"Your user {active_user['username']} has been saved\n")
      
        return active_user
    else:  # Used when no valid menu option is selected. Call function to let user try again.
        colors.print_text_color_red(
            f"{selected_option} is not a valid menu option. Please try again."
        )
        return get_active_user()