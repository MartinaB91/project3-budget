"""
Main
"""
import users
import utils
import budget
import entries
import colors

# Constants used for menu options.
CREATE_BUDGET_OPTION = "1"
ADD_PURCHASE_OPTION = "2"
GET_SUMMARY_OPTION = "3"
END_BUDGET_OPTION = "4"


def start_program():
    """Starts the program, let the user log in and
    restarts program after ended user operation."""
    active_user = users.get_active_user()

    while True:  # Infinity loop
        select_menu_option(active_user)


def select_menu_option(active_user):
    """Present user with menu options over what choises they have
    and what they can do in this program."""
    colors.print_text_color_yellow("What do you want to do? \n")
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
    user_has_budget = utils.check_if_user_has_budget(active_user["id"])

    # Depending on what choice the user choose it will lead to
    # different 'pages'. Each page has it's own function.
    if selected_option == CREATE_BUDGET_OPTION:
        budget.create_budget(active_user["id"])
    elif selected_option == ADD_PURCHASE_OPTION and user_has_budget:
        entries.save_budget_entry(active_user["id"])
    elif selected_option == GET_SUMMARY_OPTION and user_has_budget:
        budget.get_budget_summary(active_user["id"])
    elif selected_option == END_BUDGET_OPTION and user_has_budget:
        utils.change_status_budget(active_user["id"])
    elif user_has_budget is False:
        colors.print_text_color_red(
            "Please choose menu option 1 to create a budget."
            )
    else:
        colors.print_text_color_red(
            f"{selected_option} is not a valid menu option,"
            " please try again!\n"
        )


start_program()
