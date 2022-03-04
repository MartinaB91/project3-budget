import gspread
from google.oauth2.service_account import Credentials
import colors


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('budgets_db')


def save_data_to_worksheet(worksheet_name, data):
    """ Saves data to selected worksheet using parameters.
    """
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data)  # Appends list to selected worksheet


def get_all_info_from_worksheet(worksheet_name):
    """ Gets all info from selected worksheet in budgets_db. Returns list. 
    """
    worksheet = SHEET.worksheet(worksheet_name)
    data = worksheet.get_all_records()
    return data


# Todo: Change so if the sheet is empty user_id = 1
def give_data_id(worksheet_name):  
    """ Gives the data a unique id by adding 1 to the last number in lenght """
    data_in_worksheet = get_all_info_from_worksheet(worksheet_name)
    # Counts number of users and adds one to get unique id. 
    new_id = len(data_in_worksheet) + 1   
    return new_id


def get_active_budget(active_user):
    """ Get active users budget(s) and prints them so the user 
    can choose budget before making an entry."""
    all_budgets = get_all_info_from_worksheet('budgets')
    menu_option = 0

    # Used for storing only the active users budget(s).
    active_user_budgets = []
   
    for i in range(len(all_budgets)): 
        """ Loops through all budgets to find active users budget(s). 
        If a budget has the same user id as the active user,
        the budget is appended to list. 
        """
        if all_budgets[i]['user_id'] == active_user:
            active_user_budgets.append(all_budgets[i])
            menu_option = menu_option + 1

            """Because a user can have any number of budgets. 
            The menu options need to be changeable.
            """
            menu_options = f"{menu_option}. {all_budgets[i]['budget_name']} [{all_budgets[i]['status']}]\n"
            colors.print_text_color_blue(menu_options)

    try_again = True
    while try_again:
        selected_option = get_input_only_digits(f"Please select a menu option: 1-{menu_option} \n", 'Your option can only contain digits, please try again!')
        budget_index = int(selected_option) - 1  # Index is always off by one. To get index value, subtract one from selected option.
        # Inspiration from: https://www.tutorialkart.com/python/python-range/python-if-in-range/
        if budget_index in range(0, menu_option):
            try_again = False
        else:
            #  Prints text of error message in color red.
            colors.print_text_color_red(f"{selected_option} is not a valid menu option. Please try again.\n")

    active_budget = active_user_budgets[budget_index]
    return active_budget


# https://docs.python.org/2/library/stdtypes.html
def get_input_only_letters(print_statement_enter, print_statement_error_message):
    """ Check if user input is only letters. 
    If not, tell user and keep asking for input """
    try_again = True
    while try_again:
        user_input = input(print_statement_enter)
        if user_input.isalpha():
            try_again = False
        else:
            colors.print_text_color_red(print_statement_error_message)
    return user_input


# https://docs.python.org/2/library/stdtypes.html
def get_input_only_digits(print_statement_enter, print_statement_error_message):
    """ Check if user input is only digits. 
    If not, tell user and keep asking for input """
    try_again = True
    while try_again:
        user_input = input(print_statement_enter)
        if user_input.isdigit():
            try_again = False
            if user_input.startswith('0'):  # Checks if first digit is zero. Try again if it is. 
                colors.print_text_color_red("Your amount can't start with 0, please try again!")
                try_again = True
        else:
            colors.print_text_color_red(print_statement_error_message)
    return user_input


def change_status_budget(active_user_id):
    """ Changes status on active budgets to inactive.
    """
    colors.print_text_color_purple('Wich budget do you want to end?\n')
    active_budget = get_active_budget(active_user_id)  # Choosen active budget
    worksheet = SHEET.worksheet('budgets')
    worksheet.update('H' + str(active_budget['id'] + 1), 'inactive')
    colors.print_text_color_green(f"Your budget {active_budget['budget_name']} is now ended \n")