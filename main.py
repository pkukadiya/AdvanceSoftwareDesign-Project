def menu():
    print("For Spending choose 1")
    print("For Transaction choose 2")
    print("For Categories choose 3")
    print("For Exit choose 0")


# Category menu
def optcategory():
    print("For list Categories choose 1")
    print("For add new Categories choose 2")
    print("For Main Menu choose 0")


def category():
    list_category = ["Cloths", "Eating Out", "Entertainment", "Fuel",
                     "General", "Gifts", "Holiday", "Kids", "Shopping",
                     "Sports", "Travel", ]
    optcategory()
    a = int(input("Enter your choice: "))
    while a != 0:
        if a == 1:
            print(list_category)
        elif a == 2:
            print("Transaction is select")
            a = input("Enter the name of Category")
            list_category.append(a)
        else:
            print("Invalid Input! Please try again")

    print()
    menu()
    a = int(input("Enter your input"))


menu()
option = int(input("Enter your input"))
while option != 0:
    if option == 1:
        print("Spending is select")
    elif option == 2:
        print("Transaction is select")
    elif option == 3:
        category()
    else:
        print("Invalid Input! Please try again")

    print()
    menu()
    option = int(input("Enter your input"))

print("Thanks for using program. GoodBye :)")
