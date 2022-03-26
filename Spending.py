from Category import Category
from Transaction import Transaction
from datetime import datetime
class Spending:

    def current_date(self):
        #Reference for get date from user
        # https://www.w3schools.com/python/python_datetime.asp

        your_date = input("Enter date in given format yyyy-mm-dd: ")

        # Create date object in given time format yyyy-mm-dd
        my_date = datetime.strptime(your_date, "%Y-%m-%d")

    def expense(self):
        #s1 = Spending()
        #self.date()
        c1 = Category()
        t1 = Transaction()
        c1.cat_print()
        choose_cat = int(input("Choose category Between 0 To 4: "))
        a1 = c1.list_category[choose_cat]

        your_date = input("Enter date in given format yyyy-mm-dd: ")
        # Create date object in given time format yyyy-mm-dd
        my_date = datetime.strptime(your_date, "%Y-%m-%d")

        amount = int(input("Enter Amount: "))
        a2 = c1.list_budget[choose_cat] - amount
        c1.add_budget(choose_cat,a2)
        #print(a1, a2, my_date)
        note = input("Enter Note: ")
        #t1.add_notes(choose_cat,note)
        print(amount, choose_cat, note, my_date)

    def income(self):
        c1 = Category()
        c1.cat_print()
        choose_cat = int(input("Choose category Between 0 To 4: "))
        a1 = c1.list_category[choose_cat]
        self.current_date()
        amount = int(input("Enter Amount: "))
        a2 = c1.list_budget[choose_cat] + amount
        c1.add_budget(choose_cat, a2)
        print(a1, a2)
        note = input("Enter Note: ")
        print(amount, choose_cat, note)

