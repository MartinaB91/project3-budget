"""
Holds functions related to budget
"""
import utils
import colors


def create_budget(active_user):
    """ Used for creating a new budget. The user writes
    name of budget, sum of how much they want to spend."""
    colors.print_text_color_purple("Let's create a new budget!\n")

    """
    As long as chosen budget name is empty or only
    contains spaces ask for new budget name.
    """
    try_again = True
    while try_again is True:
        budget_name = input(
            f'{colors.Colors.pink}Give your budget a name:'
            f'{colors.Colors.white}\n'
            )
        if len(budget_name) != 0 and budget_name.isspace() is False:
            try_again = False
        else:
            colors.print_text_color_red(
                "Your budget name can't be empty or only contain spaces!"
                )

    colors.print_text_color_purple(
        f"The name of your new budget is {budget_name}."
        " Now let's enter the amount for each category.\n"
    )
    sum_shopping = utils.get_input_only_digits(
        f'{colors.Colors.pink}'
        'How much do you want to budget for shopping?'
        f'{colors.Colors.white}\n',
        'Your amount can only contain digits, please try again!'
        )
    sum_food = utils.get_input_only_digits(
        f'{colors.Colors.pink}'
        'How much do you want to budget for food?'
        f'{colors.Colors.white}\n',
        'Your amount can only contain digits, please try again!'
        )
    sum_entertainment = utils.get_input_only_digits(
        f'{colors.Colors.pink}'
        'How much do you want to budget for entertainment?'
        f'{colors.Colors.white}\n',
        'Your amount can only contain digits, please try again!'
        )
    sum_other = utils.get_input_only_digits(
        f'{colors.Colors.pink}'
        'How much do you want to budget for other things?'
        f'{colors.Colors.white}\n',
        'Your amount can only contain digits, please try again!'
        )
    new_budget_id = utils.give_data_id('budgets')
    sum_total = [
        new_budget_id,
        active_user,
        budget_name,
        sum_shopping,
        sum_food,
        sum_entertainment,
        sum_other,
        'active'
        ]
    utils.save_data_to_worksheet('budgets', sum_total)
    colors.print_text_color_green(
        '\nYour budget is as follows:\n'
        f'Shopping: {sum_shopping:>15}\n'
        f'Food: {sum_food:>19}\n'
        f'Entertainment: {sum_entertainment:>10}\n'
        f'Other: {sum_other:>18}\n'
        )


def get_budget_summary(active_user_id):
    """
    Gets all entries in active budget, summarize and print.
    """
    colors.print_text_color_purple(
        'Which budget would you like a summary of?\n'
        )
    active_budget = utils.get_active_budget(active_user_id)
    all_budget_entries = utils.get_all_info_from_worksheet('budget entries')

    active_budget_entries = []

    for i in range(len(all_budget_entries)):
        """
        Loops through all budgets entries to find
        active budget entries.If a budget entry has the
        same budget id as the active budget, the entry is appended to list.
        """
        if all_budget_entries[i]['budget_id'] == active_budget['id']:
            active_budget_entries.append(all_budget_entries[i])

    sum_shopping = 0
    sum_food = 0
    sum_entertainment = 0
    sum_other = 0

    for i in range(len(active_budget_entries)):
        """
        Loops through active budget entries and sort/summarize every
        entry in a variable depending on which budget category it belongs to.
        """
        if all_budget_entries[i]['category'] == 'shopping':
            sum_shopping = sum_shopping + all_budget_entries[i]['amount']
        if all_budget_entries[i]['category'] == 'food':
            sum_food = sum_food + all_budget_entries[i]['amount']
        if all_budget_entries[i]['category'] == 'entertainment':
            sum_entertainment = (
                sum_entertainment + all_budget_entries[i]['amount']
            )
        if all_budget_entries[i]['category'] == 'other':
            sum_other = sum_other + all_budget_entries[i]['amount']

    colors.print_text_color_green(
        '\nYour have spent following on:\n'
        f"Shopping: {sum_shopping:>15} of total {active_budget['shopping']}\n"
        f"Food: {sum_food:>19} of total {active_budget['food']}\n"
        f"Entertainment: {sum_entertainment:>10} of total"
        f" {active_budget['entertainment']}\n"
        f"Other: {sum_other:>18} of total {active_budget['other']}\n"
        )
