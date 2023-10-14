# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import date, time, datetime, timedelta
from pprint import pprint
import math
import random


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
today = date.today()

def get_last_five_sales_entries():
    """
    print the last 5 sales entries
    """
    print(sales[-5:])

def append_today_sales():
    """
    Appending the last row in the sheet
    """
    print("Please enter today's sale in the following order:")
    print("Cheeseburger,	Smash Burgers,	Jalapeño Popper Burgers,	Greek Stuffed Turkey Burgers,	Slutty Vegan's One Night Stand Burger,	Meat Lover's Veggie Burger,	Best-Ever Lamb Burger,	Cola,	Fanta,	7UP,	Cola-Zero,	Apfelschorle, Fries")
    print("Example- 213,122,178,73,80,113,137,187,121,101,60,70,650\n")
    while True:
        data_str = input("Enter the values in the respective order seperated with commas:")
        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("Data valid")
            break
    
    sales_d = [today.strftime("%m/%d/%Y")]+sales_data
    SHEET.worksheet("sales").append_row(sales_d)
    surplus_data(sales_data)
    print("Sales worksheet updated..........")

def update_stock(a):
    """
    Getting the column variable for calculating the average by removing the date & heading side of the sheet
    """
    pprint(a)
    print("done")
    
    


def surplus_data(dta):
    stock= SHEET.worksheet("stocks").get_all_values()
    last_stock_row = stock[-1]
    last_stock_row = last_stock_row[1:]
    surplus_data1=[]
    for stock in last_stock_row:
        surplus_data1.append(int(stock))
    sltemp=SHEET.worksheet("sales")
    temp=[]
    for i in range(2,15):
        temp2=sltemp.col_values(i)
        temp.append(temp2[-5:])
    pprint(temp)
    temp_avg=[]
    for srow in temp:
        avg=0
        for s in srow:
            avg+=int(s)
        avg=(avg/5)
        temp_avg.append(math.floor(avg))
    print("AverageDone")
    update_stock(temp_avg)




def update_last_sales_entries(s):
    """
    This funtion is either to input today's sales entry or edit
    """
    column = s[-1]
    print(column[0])
    date_object = datetime.strptime(column[0], '%m/%d/%Y').date()
    
    if today == date_object : 
        """
         Checking if the data was already inputted
        """
        edit_last_input(column,len(s))
    elif (today-date_object) == timedelta(days = 1):
        """
         Inputting the new line to the sales list & update the stock
        """
        print("append")
        append_today_sales()
    else:
        """
         Automating to fill up for the rest of the dates between today and last usage of the application
        """
        automate_filling_sales(today,date_object,column[1:])
        #append_today_sales()
    
def automate_filling_sales(tdy,last_update_date, col):
    f_days=(tdy-last_update_date).days
    
    for i in range(1, f_days):
        colmn=[]
        rand=random.uniform(0.8, 1.2)
        for j in col:
            colmn.append(math.floor(int(j)*rand))
            
        colmn.insert(0,1)
        sales_row=last_update_date+timedelta(days = i)
        print(colmn)
        #SHEET.worksheet("sales").append_row(sales_row)
        
    


def auto_append(ud):
    print(ud)


def edit_last_input(c, l):
    print("Todays update was already entered:\n", c, "\nWould you like to edit if yes please enter '1' and if not enter anykey")
    opt1 = input()
    if opt1 == '1':
        """
         We will edit the last row
        """
        SHEET.worksheet("sales").delete_rows(l)
        append_today_sales()
    else:
        print("Process cancelled......")

def validate_data(val):
    """
    This is to validate the data by converting the string to the numbers and followed by checking. This also checks whether there are 13 figures entered.
    """
    try:
        [int(v) for v in val]
        if len(val) != 13:
            raise ValueError(
              f"Exactly 13 values required, provided {len(val)}"     
             )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True



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
   print("Please enter the an option '1' for updating today's sale, '2' to print the last 5 day sales, '3' for printing the upcoming stock update")
   opt = input()
   if opt=='1':
    update_last_sales_entries(sales)
   elif opt=='2':
    get_last_five_sales_entries()
   elif opt=='3':
    get_last_stocks()
    

main()