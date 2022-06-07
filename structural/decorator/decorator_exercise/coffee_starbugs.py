import abc


class Coffee(abc.ABC):

    @abc.abstractproperty
    def price(self):
        """returns price of coffee"""

    @abc.abstractproperty
    def description(self):
        """returns description of coffee"""

    @abc.abstractmethod
    def prepare(self):
        """prepares a coffee"""


class BaseCoffee(Coffee):

    def __init__(self, price, description):
        self.__price = price
        self.__description = description

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description


class Espresso(BaseCoffee):

    def __init__(self, price=4.0):
        super().__init__(price, "Espresso")

    def prepare(self):
        print("Making a perfect espresso: 8g of coffee, 96 Celsius, 16 bar")


class Cappuccino(BaseCoffee):

    def __init__(self, price=6.0):
        super().__init__(price, "Cappuccino")

    def prepare(self):
        print("Making an espresso combined with a perfect milk foam")


class Latte(BaseCoffee):

    def __init__(self, price=9.0):
        super().__init__(price, "Latte")

    def prepare(self):
        print("Making a perfect latte")

# CENY DODATKÓW:
# Whipped: 2.5
# Whisky: 10.0
# ExtraEspresso: 4.0
