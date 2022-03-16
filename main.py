import self as self

from Category import Category


def menu(self):
    print("For Spending choose 1")
    print("For Transaction choose 2")
    print("For Categories choose 3")
    print("For Exit choose 0")

    option = int(input("Enter your input"))

    while option != 0:
        if option == 1:
            print("Spending is select")
        elif option == 2:
            print("Transaction is select")
        elif option == 3:
            #print("Transaction is select")
            Category().category_menu()
        elif option != 0:
            print("Invalid Input! Please try again")
            option = int(input("Enter your input: "))
    print("Thanks for using program. GoodBye :)")


menu(self)
