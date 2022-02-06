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
    worksheet.append_row(data)

def get_all_info_from_worksheet(worksheet_name):
    """ Gets all info from selected worksheet in budget_db. Returns list. """
    worksheet = SHEET.worksheet(worksheet_name)
    data = worksheet.get_all_records()
    return data
