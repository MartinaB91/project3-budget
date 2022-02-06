import gspread
from google.oauth2.service_account import Credentials
import utils

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('budgets_db')

def save_new_user_to_worksheet(): 
    """ Reads user inputs, give the user a unique id and save user 
    input in list and later appends list to worksheet. """
    users_in_worksheet = utils.get_all_info_from_worksheet('users',SHEET)
    new_user_id = len(users_in_worksheet) +1 # Counts number of users and adds one to get unique id. 
    user_fname = input("Enter your firstname: \n")
    user_lname = input("Enter your lastname: \n")
    username = input("Enter your username: \n")
    user = [new_user_id, username, user_fname, user_lname]
    utils.save_data_to_worksheet('users', user, SHEET) 
    return username

def get_active_user():
    """ Prints user menu options and let the user enter a username. 
    Depending on user selection the function return active user(old or new user)."""
    menu_options = ("Welcome to your budget program \n1. Enter your username. \n2. Create a new user.")
    print(menu_options)
    selected_option = input("Please select a menu option (1-2): \n")

    if selected_option == "1":
        active_user = input("Enter your username: \n")
        return active_user
    elif selected_option == "2":
        active_user = save_new_user_to_worksheet()
        return active_user
    else: # Used when no valid menu option is selected. Call function to let user try again. 
        print(f"{selected_option} is not a valid menu option. Please try again.")
        get_active_user()

# def get_all_users():
#     """ Gets all users from budget_db. Returns list. """
#     users_worksheet = SHEET.worksheet('users')
#     all_users = users_worksheet.get_all_records()
#     return all_users


