import users
import utils

def create_budget():
    """ Used for creating a new budget. The user writes
    name of budget, sum of how much they want to spend."""
    print("Let's create a new budget!")

    budget_name = input("Give your budget a name: \n")
    print(
        f"The name of your new budget is {budget_name}. Now let's enter the amount for each category."
    )
    sum_shopping = input("How much do you want to budget for shopping? \n")
    sum_food = input("How much do you want to budget for food? \n")
    sum_entertainment = input("How much do you want to budget for entertainment? \n")
    sum_other = input("How much do you want to budget for other things? \n")
    new_budget_id = utils.give_data_id('budgets')
    sum_total = [new_budget_id, "1", budget_name, sum_shopping, sum_food, sum_entertainment, sum_other]
    utils.save_data_to_worksheet('budgets', sum_total) 
    print(f"Your budget is as follows: \nShopping: {sum_shopping:>15} \nFood: {sum_food:>19} \nEntertainment: {sum_entertainment:>10} \nOther things: {sum_other:>11}")

def start_program():
    """ Present user with menu options over what choises they have 
    and what they can do in this program. """
    active_user = users.get_active_user()
    menu_options = (f"What do you want to do {active_user}? \n"
    "1. Create a new budget. \n"
    "2. Add purchase to ongoing budget. \n"
    "3. Get a summary of ongoing budget. \n"
    "4. End ongoing budget. \n")
    print(menu_options)
    
    selected_option = input("Please select a menu option (1-4): \n")
    """ Depending on what choice the user choose it will lead to 
    different 'pages'. Every page has its own function. """
    if selected_option == "1":
        create_budget()
    elif selected_option == "2":
        print(selected_option)
    elif selected_option == "3":
        print(selected_option)
    elif selected_option == "4":
        print(selected_option)
    else:
        print(f"{selected_option} is not a valid menu option. Please try again.")
        selected_option = input("Please select a menu option (1-4): \n") # Todo: Add call to function to start over.

start_program()


