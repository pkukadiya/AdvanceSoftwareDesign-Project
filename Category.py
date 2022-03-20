class Category:
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

    list_budget = [0,0,0,0,0,0,0,0,0,0,0]


    def add_budget(self, catID, budget):
        self.list_budget[catID] = budget


    def cat_print(self):
        # Print Category with index
        for i in self.list_category:
            print(str(self.list_category.index(i))+" : "+ i + " : " + str(self.list_budget[self.list_category.index(i)]))

    def add_cat(self,new_cat):
        self.list_category.append(new_cat)
        self.list_budget.append(0)





