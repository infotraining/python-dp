import abc
from dataclasses import dataclass


class InsufficientFunds(Exception):
    pass

@dataclass
class AccountContext:
    id: int
    balance: float

class AccountState(abc.ABC):
    @abc.abstractmethod
    def deposit(self, account_context: AccountContext, amount):
        pass

    @abc.abstractmethod
    def withdraw(self, account_context: AccountContext, amount):
        pass

    @property
    @abc.abstractmethod
    def state_description(self):
        pass


class StateBase(AccountState):
    def deposit(self, account_context: AccountContext, amount):
        account_context.balance += amount


class NormalState(StateBase):
    def withdraw(self, account_context: AccountContext, amount: int):
        account_context.balance -= amount

    @property
    def state_description(self):
        return "Normal"


class OverdraftState(StateBase):
    def withdraw(self, account, amount: int):
        raise InsufficientFunds()

    @property
    def state_description(self):
        return "Overdraft"


class BankAccount:
    def __init__(self, id, balance=0.0):
        self.context = AccountContext(id, balance)
        self._update_state()

    def _update_state(self):
        if self.context.balance >= 0:
            self.__state = NormalState()
        else:
            self.__state = OverdraftState()

    @property
    def balance(self):
        return self.context.balance

    @property
    def state_description(self):
        return self.__state.state_description
        
    def deposit(self, amount):
        self.__state.deposit(self.context, amount)
        self._update_state()

    def withdraw(self, amount):
        self.__state.withdraw(self.context, amount)
        self._update_state()
