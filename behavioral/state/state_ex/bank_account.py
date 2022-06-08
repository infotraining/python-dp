
class BankAccount:

    def __init__(self, id, balance=0.0):
        self.id = id
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def state_description(self):
        return "Normal" if self.balance >= 0 else "Overdraft"

    def deposit(self, amount):
        self.__balance += amount