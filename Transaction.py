from Category import Category
class Transaction:
    list_notes = []

    def add_notes(self, catID, notes):
        self.list_notes[catID] = notes

    def edit_transaction(self):
        c1 = Category()
        c1.cat_print()


