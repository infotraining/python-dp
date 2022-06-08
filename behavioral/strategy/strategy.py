    from abc import ABC, abstractmethod
    from collections import namedtuple

    Customer = namedtuple('Customer', 'name fidelity')


    class LineItem:
        def __init__(self, product, quantity, price):
            self.product = product
            self.quantity = quantity
            self.price = price

        def total(self):
            return self.price * self.quantity

    class Order:  # Context
        def __init__(self, customer, cart, promotion = None):
            self.customer = customer
            self.cart = list(cart)
            self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC): # Strategy: an abstract base class
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""
        
class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""
    
class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""
    
class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""