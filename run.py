# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import date, time, datetime, timedelta
from pprint import pprint


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
stock = SHEET.worksheet("stocks").get_all_values()

def get_last_five_sales_entries():
    """
    print the last 5 sales entries
    """
    print(sales[-5:])


def update_last_sales_entries(s):
    """
    This funtion is either to input today's sales entry or edit
    """
    column = s[-1]
    print(column[0])
    date_object = datetime.strptime(column[0], '%m/%d/%Y').date()
    today = date.today()
    if today==date_object:
        """
         Checking if the data was already inputted
        """
        edit_last_input(column,len(s))
    elif (today-date_object) == timedelta(days = 1):
        """
         Inputting the new line to the sales list & update the stock
        """
        today = today.strftime("%m/%d/%Y")
        print("yesterday")
    else:
        """
         Automating to fill up for the rest of the dates between today and last usage of the application
        """
        print(today-date_object)
    

def edit_last_input(c, l):
    print("Todays update was already entered:\n", c, "\nWould you like to edit if yes please enter '1' and if not enter anykey")
    opt1 = input()
    if opt1 == '1':
        """
         We will edit the last row
        """
        SHEET.worksheet("sales").delete_rows(l)
        print("Edit")




def get_last_stocks():
   """
   print the last stock entry
   """
   print(stock[-1])
    


def main():
   """
   Selecting the options
   Executing all the functions
   """
   print("Please enter the an option '1' for updating today's sale, '2' for printing the last 5 day sales, '3' for printing the upcoming stock update")
   opt = input()
   if opt=='1':
    update_last_sales_entries(sales)
   elif opt=='2':
    get_last_five_sales_entries()
   elif opt=='3':
    get_last_stocks()
    

#get_last_five_sales_entries()
main()