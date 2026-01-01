import pandas as pd
from datetime import datetime

# This function reads expense data from CSV file.
# If the file does not exist, it creates a new one.
def read_ex_data():
    try:
        ex = pd.read_csv("expense_data.csv")
    except FileNotFoundError:                
        # Creating an empty expense file if not found
        ex_0 = {"date":[], "category":[], "amount":[],"description":[]}
        pd.DataFrame(ex_0).to_csv("expense_data.csv", index=False)
        ex = pd.read_csv("expense_data.csv")
    return(ex)

# This function adds a new expense entry to the DataFrame
def add_ex(ex):
    while True:
        try:
            # Taking user input for expense details
            new_row = {
            "date":(datetime.strptime(
                input("Date of expense (YYYY-MM-DD): "),'%Y-%m-%d').date()),
            "category":(input("Category: ")),
            "amount":(float(input("Amount spent in Rs: "))),
            "description":(input("A brief description: ")),
            }
            break
        except ValueError:
            # Handling invalid input format
            print("\nInvalid format!! Please enter the details in the given format: \n")

    # Adding the new expense as a new row
    ex.loc[len(ex)] = new_row
    return(ex)       

# This function displays all recorded expenses
def view_ex(ex):
    print(ex)

# This function tracks total expenses and compares them with the budget
def track_bud(ex,budget):
    print("\nYour Budget for this month is: ",budget)

    expense = 0
    # Calculating total expense amount
    for i in range(len(ex['amount'])):
        expense += ex['amount'][i]

    print("Your total expenses for this month are: ",expense)

    # Checking if expenses exceed budget
    if expense>budget:
        print("WARNING..!! Your expenses have exceeded your budget! ")
        print("To update your budget enter 'y'\n Else enter any key to continue")
        key = input("Enter your choice: ")
        if key=='y':
            return(float(input("Please enter your updated budget for this month: ")))

    # Calculating remaining savings
    saving = budget - expense
    print("\nYour remaining balance for this month is: ",saving)
    return budget

# This function saves expense data to CSV file
def save_ex(ex):
    ex.to_csv('expense_data.csv', index=False)
    print("Data saved to expense_data.csv")


print("*** Welcome to the Personal Expense Tracker ***\n")

# Reading existing expense data
ex = read_ex_data()

# Taking monthly budget from user
bud = float(input("Please enter your budget for this month: \n"))

while True:
    # Displaying menu options
    print('''
To add expense Enter: 1
To view expenses Enter: 2
To Track budget Enter: 3
To Save expenses Enter: 4
To Exit Enter: 5 ''')

    while True:
        response1 = (input("\n choice: "))
        try:            
            response= int(response1)
            # Validating menu input
            if response in range(1,6):
                break
            else:
                print("\n Invalid input..!! Please select between 1 to 5")
        except ValueError:
             print("\n Invalid input..!! Please select between 1 to 5")    

    # Performing action based on user choice
    if response==1:
        ex=add_ex(ex)
    elif response==2:        
        view_ex(ex)        
    elif response==3:
        bud=track_bud(ex,bud)
    elif response==4:
        save_ex(ex)
    else:
        break





