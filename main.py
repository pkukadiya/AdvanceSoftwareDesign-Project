# import from class
from Category import Category
from Spending import Spending
from Transaction import Transaction

# Function for menu printing
def opt_spending():
    print()
    print("+++++SPENDING MENU+++++")
    print()
    print("Choose 1 for Expense: ")
    print("Choose 2 for Income: ")
    print("Choose 0 for Main Menu: ")

# Function for menu printing
def expense_menu():
    print()
    print("+++++EXPENSE MENU+++++")
    print()
    #print("Enter Date: ")
    i1 = Spending()
    # Call expense function by creating spending class object
    i1.expense()

# Function for menu printing
def income_menu():
    print()
    print("+++++INCOME MENU+++++")
    print()
    # Call expense function by creating spending class object
    i1 = Spending()
    i1.income()
    print()


def spending_menu():
    print()
    opt_spending()
    s = int(input("Choose any option: "))
    print()

    if s == 1:
        expense_menu()
    elif s == 2:
        income_menu()
    elif s == 0:
        menu()
    else:
        print("Invalid Input!! Please enter a valid input..")
        spending_menu()


def opt_transaction():
    print()
    print("+++++TRANSACTION MENU+++++")
    print()
    print("Choose 1 for List Transaction: ")
    print("Choose 2 for Edit Transaction: ")
    print("Choose 3 for Delete Transaction: ")
    print("Choose 0 for Main Menu: ")

def transaction_menu():
    print()
    # creating class object
    s1 = Spending()
    t1 = Transaction()
    opt_transaction()
    t = int(input("Choose any option: "))
    print()

    if t == 1:
        t1.trans_print(s1.list_of_cat,s1.list_dates,s1.list_amount,s1.list_notes)
    elif t == 2:
        s1.edit_transaction()
    elif t == 3:
        s1.del_transaction()
    elif t == 0:
        menu()
    else:
        print("Invalid Input!! Please enter a valid input..")
        transaction_menu()


def opt_category():
    print()
    print("+++++CATEGORY MENU+++++")
    print()
    print("Choose 1 for list Categories: ")
    print("Choose 2 for add new Categories: ")
    print("Choose 3 for add budget by each Categories: ")
    print("Choose 0 for Main Menu: ")


def category_menu():
    # b = len(list_category())
    # switch(a)
    print()
    opt_category()
    a = int(input("Enter your choice: "))

    if a == 1:
        c1 = Category()
        c1.cat_print()
    elif a == 2:
        c1 = Category()
        # print("Add new Category:")
        a = input("Enter the name of New Category: ")
        c1.add_cat(a)
        print("New Category added successfully")
        print("+++ Here is New list of Category +++")
        c1.cat_print()
    elif a==3:
        c1 = Category()
        c1.cat_print()
        print()
        cat_number = int(input("Choose category number from above list: "))
        bud = int(input("Add New Budget: "))
        c1.add_budget(cat_number, bud)
        c1.total_budget(cat_number,bud)
    elif a == 0:
        menu()
    else:
        print("Invalid Input! Please try again")
        # Category menu

def menu():
    print()
    print("+++++MAIN MENU+++++")
    print()
    print("For Spending choose 1")
    print("For Transaction choose 2")
    print("For Categories choose 3")
    print("For Progress choose 4")
    print("For Exit choose 0")
    print()
    option = int(input("Enter your choice: "))

    while True:
        if option == 1:
            #print("\"Spending is selected\"")
            spending_menu()
        elif option == 2:
            #print("\"Transaction is selected\"")
            transaction_menu()
        elif option == 3:
            #print("\"Category is selected\"")
            category_menu()
        elif option == 4:
            s1 = Spending()
            print("\"Progress is here...\"")
            s1.progress()

        elif option == 0:
            exit()
        else:
            print("Invalid Input! Please try again")
            menu()
    print("Thanks for using program. GoodBye :)")


menu()


