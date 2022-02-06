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
    print(f"Your budget is as follows: \nShopping: {sum_shopping:>15} \nFood: {sum_food:>19} \nEntertainment: {sum_entertainment:>10} \nOther things: {sum_other:>11}")
