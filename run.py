import colorama
from colorama import Fore, Back, Style
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
INGRED = SHEET.worksheet("ingredients").get_all_values()
today = date.today()

def get_last_five_sales_entries():
    """
    print the last 5 sales entries
    """
    sl=sales[-5:]
    sl=[sales[0]]+sl
    for row in sl:
        print("{: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*row))
    print(Fore.RED+"Process executed..............\n\n")
    director()


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
    
    today = date.today()
    sales_d = [today.strftime("%m/%d/%Y")]+sales_data
    SHEET.worksheet("sales").append_row(sales_d)
    surplus_data()
    print("Sales worksheet updated..........")

def update_stock(tsale7, lstk, last_date):
    """
    Getting the column variable for calculating the average by removing the date & heading side of the sheet
    """
    last_row_stk = list_int_convertor(lstk)
    ingred = INGRED[-7:]
    total_used=[]
    total_used=usage_fn(ingred, tsale7)
    new_stock=[]
    for i, j in zip(total_used, last_row_stk):
        if ((j-i)/j) > (0.15):
            new_stock.append(j)
        else:
            new_stock.append(round(i*1.1))
        
    new_stock= round_off(new_stock)
    stock_new=[last_date]+new_stock
    SHEET.worksheet("stocks").append_row(stock_new)

def round_off(ls):
    """
    Used to round of to the nearest number divisible with 100
    """
    k=0
    for i in ls:
        ls[k]=round(ls[k]/100)+1
        ls[k] *= 100
        k+=1
    return ls
    
def usage_fn(ing, sale1):
    """
    -Used forfinding the total uasge as per last week
    -Here we have used the ingredients matrix from the ingredient sheet for calulating the total usage
    """
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

    return cumulat         
            




def surplus_data():
    """
    -This function is used to find the surplus stock
    -We also automate the stock so that the program runs without any error,
    -We also find the sum of all last week sales 
    """
    stk = STOCK
    last_stock_row = stk[-1]
    last_stock_date = last_stock_row[0]
    date_dif = datetime.strptime(last_stock_date, '%m/%d/%Y').date()-date.today()
    day_var = date_dif.days
    if day_var > 0:
        last_stock_date = last_stock_row[0]
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
            temp_row = last_stock_row[1:]
            datt1=datetime.strptime(last_stock_date, '%m/%d/%Y').date()+timedelta(days=t)
            datt=datt1.strftime("%m/%d/%Y")
            temp_row.insert(0, str(datt))
            SHEET.worksheet("stocks").append_row(temp_row)            
                       
           last_stock_row = temp_row
           last_stock_date = (datetime.strptime(last_stock_date, '%m/%d/%Y').date()+timedelta(days=t+7)).strftime("%m/%d/%Y")

    sales = SHEET.worksheet("sales").get_all_values()
    stk = SHEET.worksheet("stocks").get_all_values()
    last_stock_row = stk[-1]
    last_sales_row7 = sales[-7:]
    total_sale7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for irow in last_sales_row7:
        irow = irow[1:]
        k = 0
        for s in irow:
            total_sale7[k] += int(s)
            k+=1       
            
    last_stock_row = last_stock_row[1:]
    update_stock(total_sale7, last_stock_row, last_stock_date)






def list_int_convertor(last_row):
    """
    Function helps us to convert the string into integer format for easy calculations
    """
    surplus_data1=[]
    for sk in last_row:
        surplus_data1.append(int(sk))
    return surplus_data1

def avg_sales(req_i):
    """
    Function helps us to find the average sales in the last 30 days
    """

    sltemp = SHEET.worksheet("sales")
    temp = []
    for i in range(2,15):
        temp2 = sltemp.col_values(i)
        temp.append(temp2[req_i:])

    temp_avg = []
    for srow in temp:
        avg = 0
        for s in srow[1:]:
            avg += int(s)
        temp_avg.append(math.floor(avg))
    return temp_avg
    

def update_last_sales_entries():
    """
    This funtion is either to input today's sales entry or edit
    """
    column = sales[-1]
    date_object = datetime.strptime(column[0], '%m/%d/%Y').date()
    
    if today == date_object: 
        """
         Checking if the data was already inputted
        """
        edit_last_input(column,len(sales))
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
        append_today_sales()
    
def automate_filling_sales(tdy,last_update_date, col):
    """
    This function is used to create a junk sales projection so the program could function perfectly
    """
    f_days=(tdy-last_update_date).days+1
    for i in range(1, f_days):
        colmn=[]
        rand=random.uniform(0.8, 1.2)
        for j in col:
            colmn.append(str(math.floor(int(j)*rand)))

        colmn = [(last_update_date+timedelta(days = i)).strftime("%m/%d/%Y")] + colmn
        SHEET.worksheet("sales").append_row(colmn)
    surplus_data()
        


def edit_last_input(c, l):
    """
    Function conveys that the data entry for this week was already entered and asking you whether you want to proceed
    """
    print("Todays update was already entered:\n", c, "\nWould you like to edit if yes please enter '1' and if not enter anykey")
    opt1 = input()
    if opt1 == '1':
        """
         We will edit the last row
        """
        SHEET.worksheet("sales").delete_rows(l)
        append_today_sales()
    else:
        print(Fore.RED+"Process cancelled......\n\n")

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



def get_upcoming_stocks():
   """
   print the last stock entry
   """
   line = STOCK[-1]
   head=STOCK[0]
   head=head[1:]
   ing=INGRED[6]
   ing=ing[1:]
   ing= ing+['l','l','l','l','l','l','g']
   dat=datetime.strptime(line[0], '%m/%d/%Y').date()-today
   if dat.days < 0:
        print("Please update the previous sales data")
        director()
   else:
        print("Next Stock updation date is on:",line[0],"\n")
        line=line[1:]
        for i, j, k in zip(line, head, ing):
            if(k=='g'):
                s=round(int(i)/1000)
                print(j,"=",s,"Kg")
            elif(k=='l'):
                s=round(int(i)/1000)
                print(j,"=",s,"L")
            else:
                print(j,"=",i)
    
        print(Fore.RED+"Process executed..............\n\n")
        director()

def get_left_stocks():
    line = STOCK[-1]
    head=STOCK[0]
    head=head[1:]
    ing = INGRED[-7:]
    sal=[]
    total_used=[]
    dat=datetime.strptime(line[0], '%m/%d/%Y').date()-today
    if dat.days < 0:
        print("Please update the previous sales data")
        director()
    else:
        print("Leftout stock from this week:\n")
        t=(dat.days)-7
        line = STOCK[-2]
        line = line[1:]
        print(t)
        sal=avg_sales(t)
        total_used=usage_fn(ing, sal)
        left_stock=[]
        for l, m in zip(total_used, line):
            dif=int(m)-l
            left_stock.append(dif)
        
        ing=INGRED[6]
        ing=ing[1:]
        ing= ing+['l','l','l','l','l','l','g']
        for i, j, k in zip(left_stock, head, ing):
            if(k=='g'):
                s=(int(i)/1000)
                print(j,"=",s,"Kg")
            elif(k=='l'):
                s=(int(i)/1000)
                print(j,"=",s,"L")
            else:
                print(j,"=",i)
        
        print(Fore.RED+"Process executed..............\n\n")
        director()

    

    
def director():
    """
    This funtion is used to direct to other functions
    Selecting the options
    Executing all the functions
    """
    print(f"{Back.RED}Please enter the an option")
    print("'1' for updating today's sale, \n'2' to print the last 5 day sales \n'3' for printing the upcoming stock update \n'4' for printing the stock leftout for this week \n'5' for Exiting the application")
    opt = input()
    if opt=='1':
        update_last_sales_entries()
    elif opt=='2':
        get_last_five_sales_entries()
    elif opt=='3':
        get_upcoming_stocks()
    elif opt=='4':
        get_left_stocks()
    elif opt=='5':
        print("Program exit............")
    



def main():
   """
   This function calls the director funtion that calls for multi-function
   """
   colorama.init(autoreset= True)
   print(Fore.RED+"**********************************************************************")
   print(f"{Back.GREEN}{Fore.RED}                     WELCOME TO THE BURGER APPLICATION                ")
   print(Fore.RED+"**********************************************************************")
   director()
    
main()
