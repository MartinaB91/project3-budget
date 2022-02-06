
def save_data_to_worksheet(worksheet_name,data,SHEET):
    """ Saves data to selected worksheet using parameters.""" 
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data)

def get_all_info_from_worksheet(worksheet_name,SHEET):
    """ Gets all info from selected worksheet in budget_db. Returns list. """
    worksheet = SHEET.worksheet(worksheet_name)
    data = worksheet.get_all_records()
    return data
