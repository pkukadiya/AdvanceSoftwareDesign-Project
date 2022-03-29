from Category import Category
from Transaction import Transaction
from datetime import datetime


class Spending:
    # Make a list to store data
    list_notes = []
    list_dates = []
    list_of_cat = []
    list_amount = []

    # Create a function
    def current_date(self):
        # Reference for get date from user
        # https://www.w3schools.com/python/python_datetime.asp

        your_date = input("Enter date in given format yyyy-mm-dd: ")

        # Create date object in given time format yyyy-mm-dd
        my_date = datetime.strptime(your_date, "%Y-%m-%d")

    def expense(self):
        # Object of Category class
        c1 = Category()

        # Object of Transaction class
        t1 = Transaction()
        # Category list print
        c1.cat_print()
        choose_cat = int(input("Choose category Between 0 To 4: "))
        a1 = c1.list_category[choose_cat]
        self.list_of_cat.append(a1)
        # Reference for get date from user
        # https://www.w3schools.com/python/python_datetime.asp
        your_date = input("Enter date in given format yyyy-mm-dd: ")
        # Create date object in given time format yyyy-mm-dd
        my_date = datetime.strptime(your_date, "%Y-%m-%d")
        self.list_dates.append(my_date)
        # user entered expense amount and it substitute from budget
        amount = int(input("Enter Amount: "))
        a2 = c1.list_budget[choose_cat] - amount
        c1.add_budget(choose_cat, a2)
        self.list_amount.append(a2)
        note = input("Enter Note: ")
        self.list_notes.append(note)
        # print(amount, choose_cat ,a1 , note, my_date)

    def income(self):
        # Object of Category class
        c1 = Category()

        # Object of Transaction class
        t1 = Transaction()

        # Category list print
        c1.cat_print()
        choose_cat = int(input("Choose category Between 0 To 4: "))
        a1 = c1.list_category[choose_cat]
        self.list_of_cat.append(a1)

        # Reference for get date from user
        # https://www.w3schools.com/python/python_datetime.asp
        your_date = input("Enter date in given format yyyy-mm-dd: ")
        # Create date object in given time format yyyy-mm-dd
        my_date = datetime.strptime(your_date, "%Y-%m-%d")
        self.list_dates.append(my_date)

        amount = int(input("Enter Amount: "))
        a2 = c1.list_budget[choose_cat] + amount
        c1.add_budget(choose_cat, a2)
        self.list_amount.append(a2)

        # Enter note from user and added to list
        note = input("Enter Note: ")
        self.list_notes.append(note)

    def edit_transaction(self):
        # Object of Transaction class
        t1 = Transaction()
        # Object of Spending class
        s1 = Spending()
        # Make default function
        t1.trans_print(s1.list_of_cat, s1.list_dates, s1.list_amount, s1.list_notes)
        # Choose transaction number to Edit and convert into integer
        e = int(input("Enter Transaction number"))
        e1 = self.list_of_cat[e]
        # Append the value of transaction number
        self.list_of_cat.append(e1)
        # For new amount
        new_amount = int(input("Enter a new amount"))
        self.list_amount[e] = new_amount
        # e2 = self.list_amount[new_amount]
        # print(e2)
        # self.list_amount.append(e2)

    def del_transaction(self):
        # Object of Transaction class
        t1 = Transaction()
        # Object of Spending class
        s1 = Spending()
        # Call a function with four argument, so I don't need to import transaction class
        t1.trans_print(s1.list_of_cat, s1.list_dates, s1.list_amount, s1.list_notes)
        d = int(input("Enter Transaction number"))
        # d1 = self.list_of_cat[d]
        self.list_of_cat.clear()
