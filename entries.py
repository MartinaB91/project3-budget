import utils


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
    print(active_user_budgets[budget_index])






        
            
       
            

  


