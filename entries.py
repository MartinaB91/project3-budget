"""
Holds functions related to entries.
"""
import utils
import colors

# Constants used for menu options.
SHOPPING_OPTION = "1"
FOOD_OPTION = "2"
ENTERTAINMENT_OPTION = "3"
OTHER_OPTION = "4"
DONE_OPTION = "5"


def save_budget_entry(active_user_id):
    """
    Saves purchases to choosen active budget.
    Gives the user different entry options(menu options),
    reads user input,gives the new entry a unique id and
    save information about the entry, active user and
    budget and saves to worksheet.
    """
    colors.print_text_color_yellow(
        "Which budget would you like to add purchase to?\n"
        )
    active_budget = utils.get_active_budget(active_user_id)

    if active_budget["status"] == "active":  # Do this if budget is active.
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
            colors.print_text_color_yellow(
                f"Your current budget is {active_budget['budget_name']}."
                " Now let's choose a category for your purchase: \n"
            )
            colors.print_text_color_blue(menu_options)
            colors.print_text_color_yellow(
                '\nSelect "Done" when you want to go back to main menu.\n'
            )
            selected_option = utils.get_input_only_digits(
                "Please select a menu option (1-5): \n",
                "Your option can only contain digits, please try again!",
            )

            budget_category = ""
            budget_entry = ""

            # Prints menu options for budgets entries and reads inputs.
            if selected_option == SHOPPING_OPTION:
                budget_category = "shopping"
                budget_entry = utils.get_input_only_digits(
                    f"{colors.Colors.pink}"
                    "How much have you spent on shopping:"
                    f"{colors.Colors.white}\n",
                    "Your amount can only contain digits, please try again!",
                )
            elif selected_option == FOOD_OPTION:
                budget_category = "food"
                budget_entry = utils.get_input_only_digits(
                    f"{colors.Colors.pink}"
                    "How much have you spent on food:"
                    f"{colors.Colors.white}\n",
                    "Your amount can only contain digits, please try again!",
                )
            elif selected_option == ENTERTAINMENT_OPTION:
                budget_category = "entertainment"
                budget_entry = utils.get_input_only_digits(
                    f"{colors.Colors.pink}"
                    "How much have you spent on entertainment:"
                    f"{colors.Colors.white}\n",
                    "Your amount can only contain digits, please try again!",
                )
            elif selected_option == OTHER_OPTION:
                budget_category = "other"
                budget_entry = utils.get_input_only_digits(
                    f"{colors.Colors.pink}"
                    "How much have you spent on other:"
                    f"{colors.Colors.white}\n",
                    "Your amount can only contain digits, please try again!",
                )
            elif selected_option == DONE_OPTION:
                add_more = False
            else:
                colors.print_text_color_red(
                    f"{selected_option} is not a valid menu option,"
                    " please try again.\n"
                )
            if (
                add_more is True
                and budget_category == "shopping"
                or add_more is True
                and budget_category == "food"
                or add_more is True
                and budget_category == "entertainment"
                or add_more is True
                and budget_category == "other"
            ):
                colors.print_text_color_green(
                    "Your purchase has been saved!\n"
                    )
                # Gets the entry a unique id.
                new_budget_id = utils.give_data_id("budget entries")
                entry = [  # Saves data in a list
                    new_budget_id,
                    active_user_id,
                    active_budget["id"],
                    budget_category,
                    budget_entry,
                ]
                utils.save_data_to_worksheet("budget entries", entry)
    else:
        colors.print_text_color_red(
            "Your can only add purchases to ongoing(active) budgets."
        )
