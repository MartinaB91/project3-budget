import utils

def get_active_budget(active_user):
    """ Get active users budget(s) and prints them so the user 
    can choose budget before making an entry."""
    all_budgets = utils.get_all_info_from_worksheet('budgets')
    menu_option = 0

    for i in range(len(all_budgets)):
        if all_budgets[i]['user_id'] == active_user:
            active_user_budgets = all_budgets[i]['budget_name'] # Save name of budgets connected to active user
            menu_option = menu_option +1
            print(f"{menu_option}. {all_budgets[i]['budget_name']}\n")
            

  


