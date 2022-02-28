import utils

def create_budget(active_user):
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
    sum_total = [new_budget_id, active_user, budget_name, sum_shopping, sum_food, sum_entertainment, sum_other]
    utils.save_data_to_worksheet('budgets', sum_total) 
    print(f"Your budget is as follows: \nShopping: {sum_shopping:>15} \nFood: {sum_food:>19} \nEntertainment: {sum_entertainment:>10} \nOther: {sum_other:>11}")

def get_budget_summary(active_user_id):
    """ Gets all entries in active budget, summarize and print. """
    print('Wich budget would you like a summary of?\n')
    active_budget = utils.get_active_budget(active_user_id) 
    all_budget_entries = utils.get_all_info_from_worksheet('budget entries')

    active_budget_entries = []

    for i in range(len(all_budget_entries)): 
        """ Loops through all budgets entries to find active budget entries.
        If a budget entry has the same budget id as the active budget, the entry is appended to list. """ 
        if all_budget_entries[i]['budget_id'] == active_budget['id']:
            active_budget_entries.append(all_budget_entries[i])

    sum_shopping = 0
    sum_food = 0
    sum_entertainment = 0
    sum_other = 0        

    for i in range(len(active_budget_entries)): 
        """ Loops through active budget entries and sort/summarize every
        entry in a variable depending on wich budget category it belongs to. """
        if all_budget_entries[i]['category'] == 'shopping':
            sum_shopping = sum_shopping + all_budget_entries[i]['amount']
        if all_budget_entries[i]['category'] == 'food':
            sum_food = sum_food + all_budget_entries[i]['amount']
        if all_budget_entries[i]['category'] == 'entertainment':
            sum_entertainment = sum_entertainment + all_budget_entries[i]['amount']
        if all_budget_entries[i]['category'] == 'other':
            sum_other = sum_other + all_budget_entries[i]['amount']

            
    print(f'Your have spent following on: \nShopping: {sum_shopping:>16} of total {active_budget["shopping"]} \nFood: {sum_food:>19} of total {active_budget["food"]}\nEntertainment: {sum_entertainment:>10} of total {active_budget["entertainment"]} \nOther: {sum_other:>18} of total {active_budget["other"]}')