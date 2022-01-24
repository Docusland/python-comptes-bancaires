class Customer:
    def __init__(self, name: str):
        """ default constructor """
        self.__name = name
        self.__accounts = []

    # a getter function
    @property
    def name(self):
        return self.__name

    # a setter function
    @name.setter
    def name(self, name):
        self.__name = name

    # a getter function
    @property
    def accounts(self):
        return self.__accounts

    # a setter function
    @accounts.setter
    def accounts(self, accounts):
        self.__accounts = accounts

    def add_account(self, account) -> bool:
        self.__accounts.append(account)
        return True
