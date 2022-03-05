import users
import utils
import budget
import entries
import colors


def start_program():
    """ Starts the program, let the user log in and
    restarts program after ended user operation."""
    active_user = users.get_active_user()

    while True:  # Infinity loop
        select_menu_option(active_user)
        
    
def select_menu_option(active_user):
    """Present user with menu options over what choises they have
    and what they can do in this program."""
    colors.print_text_color_purple("What do you want to do? \n")
    menu_options = (
        "1. Create a new budget. \n"
        "2. Add purchase to ongoing budget. \n"
        "3. Get a summary of ongoing budget. \n"
        "4. End ongoing budget. \n"
    )
    colors.print_text_color_blue(menu_options)

    selected_option = utils.get_input_only_digits(
        "Please select a menu option (1-4): \n",
        "Your option can only contain digits, please try again!", 
    )
    """ Depending on what choice the user choose it will lead to 
    different 'pages'. Every page has it's own function."""
    if selected_option == "1": 
        budget.create_budget(active_user["id"])
    elif selected_option == "2":
        entries.save_budget_entry(active_user["id"])
    elif selected_option == "3":
        budget.get_budget_summary(active_user["id"])
    elif selected_option == "4":
        utils.change_status_budget(active_user["id"])
    else:
        colors.print_text_color_red(
            f"{selected_option} is not a valid menu option. Please try again.\n"
        )


start_program()
