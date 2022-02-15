import utils

def save_budget_entry(active_budget_id, active_user_id, active_budget_name):
        menu_options = (f"Your current budget is {active_budget_name}. Now let's choose a category for your purchase: \n"
        "1. Shopping. \n"
        "2. Food. \n"
        "3. Entertainment. \n"
        "4. Other. \n"
        "5. Done.")
        print(menu_options)
        selected_option = input("Please select a menu option (1-5): \n")

        if selected_option == "1":
            budget_category = "shopping"
            budget_entry = input("How much have you spent on shopping:")
        elif selected_option == "2":
            budget_category = "food"
            budget_entry = input("How much have you spent on food:")
        elif selected_option == "3":
            budget_category = "entertainment"
            budget_entry = input("How much have you spent on entertainment:")
        elif selected_option == "4":
            budget_category = "other"
            budget_entry = input("How much have you spent on other:")
        elif selected_option == "5":
            print(selected_option) # Todo: Return to start page or go back
        else:
            print(f"{selected_option} is not a valid menu option. Please try again.")
            selected_option = input("Please select a menu option (1-5): \n")
        
        new_budget_id = utils.give_data_id('budget entries')
        entry = [new_budget_id, active_user_id, active_budget_id, budget_category, budget_entry]
        utils.save_data_to_worksheet('budget entries', entry) 


def get_active_budget(active_user):
    """ Get active users budget(s) and prints them so the user 
    can choose budget before making an entry."""
    all_budgets = utils.get_all_info_from_worksheet('budgets')
    menu_option = 0

    active_user_budgets = [] # Used for storing only the active users budget(s).
   
    for i in range(len(all_budgets)): 
        """ Loops through all budgets to find active users budget(s). 
        If a budget has the same user id as the active user, the budget is appended to list. """
        if all_budgets[i]['user_id'] == active_user:
            active_user_budgets.append(all_budgets[i])
            menu_option = menu_option + 1
            
            """Because a user can have any number of budgets. 
            The menu options need to be changeable."""
            menu_options = f"{menu_option}. {all_budgets[i]['budget_name']}\n"
            print(menu_options)
    
    selected_option = input(f"Please select a menu option: 1-{menu_option} \n") 
    budget_index = int(selected_option) - 1 # Index is always off by one. To get index value, subtract one from selected option.
    active_budget = active_user_budgets[budget_index]
    save_budget_entry(active_budget['id'], active_budget['user_id'], active_budget['budget_name'])
  

    


    
   









        
            
       
            

  


