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


def create_budget():
    """ Used for creating a new budget. The user writes
    name of budget, sum of how much they want to spend."""
    print("Let's create a new budget!")
    get_active_user() # Gets the current user(new created or previous user)

    budget_name = input("Give your budget a name: \n")
    print(
        f"The name of your new budget is {budget_name}. Now let's enter the amount for each category."
    )
    sum_shopping = input("How much do you want to budget for shopping? \n")
    sum_food = input("How much do you want to budget for food? \n")
    sum_entertainment = input("How much do you want to budget for entertainment? \n")
    sum_other = input("How much do you want to budget for other things? \n")
    
    print(f"Your budget is as follows: \nShopping: {sum_shopping:>15} \nFood: {sum_food:>19} \nEntertainment: {sum_entertainment:>10} \nOther things: {sum_other:>11}")

def save_user_to_worksheet(): 
    """ Reads user inputs, give the user a unique id and save user 
    input in list and later appends list to worksheet. """
    users_in_worksheet = get_all_users()
    new_user_id = len(users_in_worksheet) +1 # Counts number of users and adds one to get unique id. 
    user_fname = input("Enter your firstname: \n")
    user_lname = input("Enter your lastname: \n")
    username = input("Enter your username: \n")
    user = [new_user_id, username, user_fname, user_lname]
    utils.save_data_to_worksheet('users', user, SHEET) 
    
def get_active_user():
    """ Prints user menu options. Calls different functions 
    depending on user selection(old or new user). """
    print("1. Enter your username. \n2. Create a new user.")
    selected_option = input("Please select a menu option (1-2): \n")

    if selected_option == "1":
        create_budget() # Todo:Get and return user id(if user already exist)
    elif selected_option == "2":
        save_user_to_worksheet()
    else: # Used when no valid menu option is selected. Call function to let user try again. 
        print(f"{selected_option} is not a valid menu option. Please try again.")
        get_active_user()
          
def get_all_users():
    """ Gets all users from budget_db. Returns list. """
    users_worksheet = SHEET.worksheet('users')
    all_users = users_worksheet.get_all_records()
    return all_users

def start_program():
    """ Present user with menu options over what choises they have 
    and what they can do in this program. """
    print("Welcome to your budget program")
    menu_options = ("What do you want to do? \n"
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

