from Category import Category
from datetime import datetime
class Spending:

    def add_expense(self):
        print("Do somthing")

    def current_date(self):
        your_date = input("enter date in given format yyyy-mm-dd: ")

        # Create date object in given time format yyyy-mm-dd
        my_date = datetime.strptime(your_date, "%Y-%m-%d")

    def spending_income(self):
        #s1 = Spending()
        #self.date()
        c1 = Category()
        c1.cat_print()
        choose_cat = int(input("Choose category Between 0 To 4: "))
        a1 = c1.list_category[choose_cat]
        amount = int(input("Enter Amount: "))
        a2 = c1.list_budget[choose_cat] - amount
        c1.add_budget(choose_cat,a2)
        print(a1, a2)
        note = input("Enter Note: ")
        print(amount, choose_cat, note)
