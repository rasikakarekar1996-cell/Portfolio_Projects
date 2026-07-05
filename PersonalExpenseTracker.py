from datetime import datetime 
import csv

#Load Expenses:
def load_file():    
    Expenses = []
    try:
        with open('Expense.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                exp = {"Date" : row['Date'],
                       "Category" : row['Category'],
                       "Amount Spent" : float(row['Amount Spent']),
                       "Description" : row['Description']}
                Expenses.append(exp)
        print('Expenses Loaded Successfully')
    except FileNotFoundError:
        print('No saved expenses file found!')
    return Expenses
#Expenses=load_file()

#1.Add Expense
def add_expense(Expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid Date! Please Enter Valid Date")
        return
    
    category = input("Enter Category of Expense: ").strip()
    if not category:
        print("Category cannot be empty!")
        return

    try:
        amount  = float(input("Enter amount spent: "))
    except ValueError:
        print("Please Enter Valid Amount")
        return
    
    descr = input("Enter Description: ").strip()
    #if not descr:
        #print("Description cannot be empty!")
        #return

    expense = {"Date" : date,
               "Category" : category,
               "Amount Spent" : amount,
               "Description" : descr}
    Expenses.append(expense)
    print("Expense added successfully ✅")
    
#2. View Expenses:
def view_expense(Expenses):
    if not Expenses:
       print('No Expenses to show!')
       return
    print("\n All Expenses: ")

    for i in Expenses:
        if(not i.get("Date") or
           not i.get("Category") or
           not i.get("Amount Spent") or
           not i.get("Description")):
            print("Incomplete Details Found! Please Enter All Details")
            continue
    
        print(f"Date:             {i['Date']}")
        print(f"Category:         {i['Category']}")
        print(f"Amount Spent:     {i['Amount Spent']}")
        print(f"Description:      {i['Description']}")

#3. Monthly Budget:
def monthly_budget():
    budget = float(input('Enter Monthly Budget: '))
    return budget
#monthly_budget()

def total_expenses(Expenses,budget):
    total = 0
    for j in Expenses:
        if not j.get("Amount Spent"):
            continue
        total += j["Amount Spent"]
    print(f"Total Expenses are: {total}")

    if budget<total:
        print('You have exceeded your budget!')
    else:
        balance = budget - total
        print(f'You have {balance} left for the month')
#budget = monthly_budget()
#total_expenses(Expenses,budget)

#4. Save Expenses:
def save_file(Expenses):
    with open('Expense.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Category','Amount Spent','Description'])
        for i in Expenses:
            writer.writerow([i.get('Date'),
                             i.get('Category'),
                             i.get('Amount Spent'),
                             i.get('Description')])
    print('Expenses Saved Successfully')

#save_file(Expenses)
#5. Interactive Menu:
def menu():
    Expenses = load_file()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense(Expenses)
        elif choice == '2':
            view_expense(Expenses)
        elif choice == '3':
            budget = monthly_budget()
            total_expenses(Expenses,budget)
        elif choice == '4':
            save_file(Expenses)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
menu()







        



        


    


