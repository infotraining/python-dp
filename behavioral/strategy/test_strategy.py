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


class Promotion(ABC):  # Strategy: an abstract base class
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class NullPromo(Promotion):
    """No discount at all"""

    def discount(self, order):
        return 0


class Order:  # Context
    def __init__(self, customer, cart, promotion=NullPromo()):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class NullPromo(Promotion):
    """No discount at all"""

    def discount(self, order: Order):
        return 0


class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order: Order):
        if order.customer.fidelity >= 1000:
            return order.total() * 0.05
        return 0


class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order: Order):
        _discount = 0
        for line_item in order.cart:
            if line_item.quantity >= 20:
                _discount += line_item.total() * 0.1

        return _discount


class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order: Order):
        if len(order.cart) >= 10:
            return order.total() * 0.07
        return 0


# Composite Pattern for Promotion Strategy
class PromotionGroup(Promotion):
    def __init__(self):
        self._promos = []

    def add_promo(self, promo: Promotion):
        self._promos.append(promo)

    def discount(self, order):
        return max((promo.discount(order) for promo in self._promos), default=0)


def test_fidelity_promo():
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5), LineItem(
        'apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]

    order = Order(ann, cart, FidelityPromo())

    assert order.due() == 39.90


def test_bulk_promo():
    ann = Customer('Ann Smith', 0)
    bulk_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    order = Order(ann, bulk_cart, BulkItemPromo())

    assert order.due() == 28.50


def test_large_order_promo():
    ann = Customer('Ann Smith', 0)
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    order = Order(ann, long_order, LargeOrderPromo())

    assert order.due() == 9.30


def test_promo_group():

    promo_group = PromotionGroup()
    promo_group.add_promo(FidelityPromo())
    promo_group.add_promo(BulkItemPromo())

    ann = Customer('Ann Smith', 1200)
    bulk_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    order = Order(ann, bulk_cart, promo_group)

    assert order.due() == 28.50
