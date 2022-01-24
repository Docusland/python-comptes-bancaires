class Bank:

    def __init__(self, name: str):
        """ default constructor """
        self._name = name
        self._customers = []

    @property
    def name(self):
        return self.name

    @property
    def customers(self):
        return self.customers
