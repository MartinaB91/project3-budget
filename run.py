import users
import utils
import budget
import entries

def start_program():
    active_user = users.get_active_user()
    select_menu_option(active_user)


def select_menu_option(active_user):
    """ Present user with menu options over what choises they have 
    and what they can do in this program. """
    menu_options = ("What do you want to do? \n"
    "1. Create a new budget. \n"
    "2. Add purchase to ongoing budget. \n"
    "3. Get a summary of ongoing budget. \n"
    "4. End ongoing budget. \n")
    print(menu_options)
    
    selected_option = input("Please select a menu option (1-4): \n")
    """Depending on what choice the user choose it will lead to 
    different 'pages'. Every page has it's own function."""
    if selected_option == "1":
        budget.create_budget(active_user[0]['id'])
        select_menu_option(active_user)
    elif selected_option == "2":
        entries.save_budget_entry(active_user[0]['id'])
    elif selected_option == "3":
        budget.get_budget_summary(active_user[0]['id'])
    elif selected_option == "4":
        print(selected_option)
    else:
        print(f"{selected_option} is not a valid menu option. Please try again.")
        selected_option = input("Please select a menu option (1-4): \n") # Todo: Add call to function to start over.

start_program()