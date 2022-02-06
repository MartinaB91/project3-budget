
def save_data_to_worksheet(worksheet,data,SHEET):
    """ Saves data to selected worksheet using parameters.""" 
    worksheet = SHEET.worksheet(worksheet)
    worksheet.append_row(data)
