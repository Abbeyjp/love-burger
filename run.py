# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_burger')
sales = SHEET.worksheet("sales").get_all_values()


def get_last_sales_entries(s):
    column = s[-1]
    print(column[0])
    date_object = datetime.strptime(column[0], '%m/%d/%Y').date()
    print(type(date_object))
    

get_last_sales_entries(sales)

def edit_last_sales_entries():
    #SHEET.worksheet("sales").delete_rows(-1:)
    column = SHEET.worksheet("sales").max_row
    print(column[0])
    
edit_last_sales_entries()