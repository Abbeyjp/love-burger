# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import date, time, datetime, timedelta
from pprint import pprint
import math
import random
from decimal import Decimal


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
STOCK = SHEET.worksheet("stocks").get_all_values()
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
    surplus_data()
    print("Sales worksheet updated..........")

def update_stock(a, tsale7, lstk, last_date):
    """
    Getting the column variable for calculating the average by removing the date & heading side of the sheet
    """
    last_row_stk = list_int_convertor(lstk)
    ingred = SHEET.worksheet("ingredients").get_all_values()
    ingred = ingred[-7:]
    total_used=[]
    total_used=usage_fn(ingred, tsale7)
    new_stock=[]
    print("hereeeeeeeeeeeeeeeeeeeeeee")
    for i, j in zip(total_used, last_row_stk):
        if ((j-i)/j) > (0.15):
            new_stock.append(j)
        else:
            new_stock.append(round(i*1.1))
        
    new_stock= round_off(new_stock)
    print(last_date, type(last_date))
    stock_new=[last_date]+new_stock
    SHEET.worksheet("stocks").append_row(stock_new)
    print("variation", new_stock)


def round_off(ls):
    k=0
    for i in ls:
        ls[k]=round(ls[k]/100)+1
        ls[k] *= 100
        k+=1
    return ls
    
def usage_fn(ing, sale1):
    cumulative=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cumulative[-1]=sale1[-1]
    cumulative[-2]=sale1[-2]
    cumulative[-3]=sale1[-3]
    cumulative[-4]=sale1[-4]
    cumulative[-5]=sale1[-5]
    cumulative[-6]=sale1[-6]
    for i, j in zip(sale1, ing):
        j=j[1:]
        looper=0
        for burger in j:
            temp=float(burger)*int(i)
            cumulative[looper]+=temp
            looper+=1
    cumulat=[]
    for k in cumulative:
        cumulat.append(int(k))


    #cumulat=[today.strftime("%m/%d/%Y")]+cumulat
    #return cumulat
    return cumulat
    #SHEET.worksheet("stocks").append_row(cumulat)
    #print("Cumulative items used", cumulat)
            
            




def surplus_data():
    stk = STOCK
    last_stock_row = stk[-1]
    last_stock_date = last_stock_row[0]
    print(last_stock_date,"Stock date")
    print(datetime.strptime(last_stock_date, '%m/%d/%Y').date()-date.today())
    date_dif = datetime.strptime(last_stock_date, '%m/%d/%Y').date()-date.today()
    day_var = date_dif.days
    print(day_var,"lllllllllllllllllllllllllll")
    if day_var > 0:
        last_stock_date = last_stock_row[0]
        print(last_stock_date,"ddddddddddddddddddddddddddddddd")
        last_stock_row = stk[-2]
        l=len(stk)
        SHEET.worksheet("stocks").delete_rows(l)
    else:
        temp_row = last_stock_row
        if day_var < (-7):
           weeks = math.floor(-1*day_var/7)
           iter=0
           while(iter < weeks):
            iter+=1
            t=iter*7
            print(t)
            temp_row = last_stock_row[1:]
            datt1=datetime.strptime(last_stock_date, '%m/%d/%Y').date()+timedelta(days=t)
            datt=datt1.strftime("%m/%d/%Y")
            temp_row.insert(0, str(datt))
            SHEET.worksheet("stocks").append_row(temp_row)            
                       
           last_stock_row = temp_row
           print(last_stock_row)
           last_stock_date = (datetime.strptime(last_stock_date, '%m/%d/%Y').date()+timedelta(days=t+7)).strftime("%m/%d/%Y")
           print("week=",weeks)

    sales = SHEET.worksheet("sales").get_all_values()
    stk = SHEET.worksheet("stocks").get_all_values()
    last_stock_row = stk[-1]
    last_sales_row7 = sales[-7:]
    temp_avg=avg_sales30()
    total_sale7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for irow in last_sales_row7:
        irow = irow[1:]
        k = 0
        for s in irow:
            total_sale7[k] += int(s)
            k+=1       
            
    last_stock_row = last_stock_row[1:]
    update_stock(temp_avg, total_sale7, last_stock_row, last_stock_date)






def list_int_convertor(last_row):
    surplus_data1=[]
    for sk in last_row:
        surplus_data1.append(int(sk))
    return surplus_data1

def avg_sales30():
    sltemp = SHEET.worksheet("sales")
    temp = []
    for i in range(2,15):
        temp2 = sltemp.col_values(i)
        temp.append(temp2[-30:])
    temp_avg = []
    for srow in temp:
        avg = 0
        for s in srow:
            avg += int(s)
        avg = (avg/30)
        temp_avg.append(math.floor(avg))
    return(temp_avg)

def update_last_sales_entries(s):
    """
    This funtion is either to input today's sales entry or edit
    """
    column = s[-1]
    date_object = datetime.strptime(column[0], '%m/%d/%Y').date()
    
    if today == date_object: 
        """
         Checking if the data was already inputted
        """
        edit_last_input(column,len(s))
    elif (today-date_object) == timedelta(days = 1):
        """
         Inputting the new line to the sales list & update the stock
        """
        append_today_sales()
    else:
        """
         Automating to fill up for the rest of the dates between today and last usage of the application
        """
        automate_filling_sales(today,date_object,column[1:])
    
def automate_filling_sales(tdy,last_update_date, col):
    """
    This function is used to create a junk sales projection so the program could function perfectly
    """
    f_days=(tdy-last_update_date).days
    for i in range(1, f_days):
        colmn=[]
        rand=random.uniform(0.8, 1.2)
        for j in col:
            colmn.append(str(math.floor(int(j)*rand)))

        colmn = [(last_update_date+timedelta(days = i)).strftime("%m/%d/%Y")] + colmn
        SHEET.worksheet("sales").append_row(colmn)
        


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
    
surplus_data()
