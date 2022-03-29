class Category:
    # Make a category and budget list
    list_category = ["Cloths",
                     "Eating Out",
                     "Entertainment",
                     "Fuel",
                     "General"]
                     # "Gifts",
                     # "Holiday",
                     # "Kids",
                     # "Shopping",
                     #  "Sports",
                     #  "Travel"

    list_budget = [0,0,0,0,0]
    list_total_budget = [0,0,0,0,0]


    def add_budget(self, catID, budget):
        # For particular category add budget
        self.list_budget[catID] = budget

    def total_budget(self, catID, total_budget):
        # For particular category total budget
        self.list_total_budget[catID] = total_budget
        print(self.list_total_budget)

    def print_budget(self):

        # for i in self.list_total_budget:
        print("Your total budget is: " + str(self.list_total_budget) + " " +str(self.list_category))
        exit()


    def cat_print(self):
        print()
        # Print Category with index
        print("CATEGORY LIST")
        print()
        for i in self.list_category:
            print(str(self.list_category.index(i))+" : "+ i + " : " + str(self.list_budget[self.list_category.index(i)]))

    def add_cat(self,new_cat):
        # For new category and budget
        self.list_category.append(new_cat)
        self.list_budget.append(0)
        self.list_total_budget.append(0)





