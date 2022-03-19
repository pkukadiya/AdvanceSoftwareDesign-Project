
class Category:

    def optcategory(self):
        print("+++++CATEGORY MENU+++++")
        print()
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

        if a == 1:
            for x in list_category:
                print(x)
            # print(list_category.values())
        elif a == 2:
            #print("Add new Category:")
            a = input("Enter the name of New Category")
            list_category.append(a)
            print("New Category added successfully")
            print("+++ Here is New list of Category +++")
            print(list_category)
        elif a==0:
            exit()
        else:
            print("Invalid Input! Please try again")
            # Category menu



