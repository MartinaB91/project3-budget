import utils
import colors


def save_budget_entry(active_user_id):
    """ 
    Saves purchases to choosen active budget.
    Gives the user different entry options(menu options), reads user input,
    gives the new entry a unique id and save information about the entry, active user and 
    budget and saves to worksheet. 
    """
    colors.print_text_color_purple('Wich budget would you like to add purchase to?\n')
    active_budget = utils.get_active_budget(active_user_id)

    if active_budget['status'] == 'active':  # Do this if budget is active. 
        add_more = True
        # Loop continues until user select option "Done".
        while add_more:
            menu_options = (
                "1. Shopping. \n"
                "2. Food. \n"
                "3. Entertainment.\n"
                "4. Other. \n"
                "5. Done."
            )
            colors.print_text_color_purple(f"Your current budget is {active_budget['budget_name']}."
            " Now let's choose a category for your purchase: \n")
            colors.print_text_color_blue(menu_options)
            selected_option = utils.get_input_only_digits('Please select a menu option (1-5): \n', 'Your option can only contain digits, please try again!')

            """ Prints menu options for budgets entries and reads inputs."""
            if selected_option == "1":
                budget_category = "shopping"
                budget_entry = utils.get_input_only_digits(f"{colors.Colors.pink}How much have you spent on shopping:{colors.Colors.white}\n", 'Your amount can only contain digits, please try again!')
            elif selected_option == "2":
                budget_category = "food"
                budget_entry = utils.get_input_only_digits(f"{colors.Colors.pink}How much have you spent on food:{colors.Colors.white}\n", 'Your amount can only contain digits, please try again!')
            elif selected_option == "3":
                budget_category = "entertainment"
                budget_entry = utils.get_input_only_digits(f"{colors.Colors.pink}How much have you spent on entertainment:{colors.Colors.white}\n", 'Your amount can only contain digits, please try again!')
            elif selected_option == "4":
                budget_category = "other"
                budget_entry = utils.get_input_only_digits(f"{colors.Colors.pink}How much have you spent on other:{colors.Colors.white}\n", 'Your amount can only contain digits, please try again!')
            elif selected_option == "5":
                add_more = False
            else:
                print(f"{selected_option} is not a valid menu option. Please try again.\n")

            if add_more == True:
                colors.print_text_color_green('Your purchase has been saved!\n')
                new_budget_id = utils.give_data_id('budget entries')  # Gets the entry a unique id 
                entry = [new_budget_id, active_user_id, active_budget['id'], budget_category, budget_entry]  # Saves data in a list
                utils.save_data_to_worksheet('budget entries', entry)
    else:
        colors.print_text_color_red('Your can only add purchases to ongoing(active) budgets.')