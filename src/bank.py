class Bank:

    def __init__(self, bank_name):
        self.customers_count = 0
        self.customers_dict = dict()
        self.bank_name = bank_name

    def add_new_customer(self,customer_name):
        self.customers_count += 1
        self.customers_dict[customer_name] = 0 # Je voudrais ensuite mettre un enum
                                                # pour savoir rapidement quel(s) type(s) de compte il possède
