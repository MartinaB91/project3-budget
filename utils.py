import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('budgets_db')

def save_data_to_worksheet(worksheet_name,data):
    """ Saves data to selected worksheet using parameters.""" 
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data) # Appends list to selected worksheet

def get_all_info_from_worksheet(worksheet_name):
    """ Gets all info from selected worksheet in budget_db. Returns list. """
    worksheet = SHEET.worksheet(worksheet_name)
    data = worksheet.get_all_records()
    return data

def give_data_id(worksheet_name): # Todo: Change so if the sheet is empty user_id = 1
    """ Gives the data a unique id by adding 1 to the last number in lenght """
    data_in_worksheet = get_all_info_from_worksheet(worksheet_name) 
    new_id = len(data_in_worksheet) +1 # Counts number of users and adds one to get unique id. 
    return new_id

def get_active_budget(active_user):
    """ Get active users budget(s) and prints them so the user 
    can choose budget before making an entry."""
    all_budgets = get_all_info_from_worksheet('budgets')
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
    return active_budget