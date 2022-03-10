
class Category:

    def optcategory(self):
        print("+++++CATEGORY MENU+++++")
        print("For list Categories choose 1")
        print("For add new Categories choose 2")
        print("For Main Menu choose 0")

    def category_menu(self):
        list_category = ["Cloths",
                         "Eating Out",
                         "Entertainment",
                         "Fuel",
                         "General",
                          "Gifts",
                          "Holiday",
                          "Kids",
                          "Shopping",
                          "Sports",
                          "Travel"]


        # b = len(list_category())
        # switch(a)

        self.optcategory()
        a = int(input("Enter your choice: "))

        while a != 0:
            if a == 1:
                for x in list_category:
                    print(x)
                # print(list_category.values())
            elif a == 2:
                print("Add new Category:")
                a = input("Enter the name of Category")
                list_category.append(a)
                print("New Category Entered successfully")
            else:
                print("Invalid Input! Please try again")
            # Category menu



