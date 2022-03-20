from Category import Category


def opt_spending():
    print("+++++SPENDING MENU+++++")
    print()
    print("Choose 1 for Expense: ")
    print("Choose 2 for Income: ")
    print("Choose 0 for Main Menu: ")


def expense_menu():
    print("+++++EXPENSE MENU+++++")
    print()
    print("Enter Date: ")
    print("Enter Amount: ")
    print("Enter category: ")
    print("Enter Note: ")
    print()


def income_menu():
    print("+++++INCOME MENU+++++")
    print()
    print("Enter Date: ")
    print("Enter Amount: ")
    print("Enter category: ")
    print("Enter Note: ")
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
    print("+++++SPENDING MENU+++++")
    print()
    print("Choose 1 for Edit Transaction: ")
    print("Choose 2 for Delete Transaction: ")
    print("Choose 0 for Main Menu: ")


def opt_category():
    print("+++++CATEGORY MENU+++++")
    print()
    print("For list Categories choose 1")
    print("For add new Categories choose 2")
    print("For add budget by each Categories choose 3")
    print("For Main Menu choose 0")


def category_menu():


    # b = len(list_category())
    # switch(a)

    opt_category()
    a = int(input("Enter your choice: "))

    if a == 1:
        c1 = Category()
        c1.cat_print()
    elif a == 2:
        c1 = Category()
        # print("Add new Category:")
        a = input("Enter the name of New Category")
        c1.add_cat(a)
        print("New Category added successfully")
        print("+++ Here is New list of Category +++")
        c1.cat_print()
    elif a==3:
        cat_number = int(input("Enter the category number that you want to add budget: "))
        bud = int(input("Add New Budget"))
        c1 = Category()
        c1.add_budget(cat_number, bud)
    elif a == 0:
        menu()
    else:
        print("Invalid Input! Please try again")
        # Category menu

def menu():
    print("+++++MAIN MENU+++++")
    print()
    print("For Spending choose 1")
    print("For Transaction choose 2")
    print("For Categories choose 3")
    print("For Exit choose 0")

    option = int(input("Enter your choice: "))

    while True:
        if option == 1:
            #print("\"Spending is selected\"")
            spending_menu()
        elif option == 2:
            #print("\"Transaction is selected\"")
            opt_transaction()
        elif option == 3:
            print("\"Category is selected\"")
            category_menu()
        elif option == 0:
            exit()
        else:
            print("Invalid Input! Please try again")
            menu()
    print("Thanks for using program. GoodBye :)")


menu()


