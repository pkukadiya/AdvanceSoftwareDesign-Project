
class Transaction:

    # Make a function with four argument
    def trans_print(self, list_of_cat, list_dates, list_amount, list_notes):
        # For print all transaction
        for i in range(0, len(list_notes)):
            print(str(i)+ " " + str(list_of_cat[i]) + " " + str(list_dates[i]) + " " + str(list_amount[i]) + " " + str(list_notes[i]))





