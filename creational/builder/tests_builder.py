class Order:
    def __init__(self, cart, 
                 billing_information, shipping_address):
        self.cart = cart
        self.billing_information = billing_information
        self.shipping_address = shipping_address
        
class Item:
    def __init__(self, guid, quantity):
        self.guid = guid
        self.quantity = quantity
        
class Address:
    def __init__(self, name, address, city, state, zipcode):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        
class BillingInformation:
    def __init__(self, billing_address, credit_card_number,
                 expiration_month, expiration_year, 
                 card_holder_name):
        self.billing_address = billing_address
        self.credit_card_number = credit_card_number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.card_holder_name = card_holder_name


class OrderBuilder:
    def __init__(self):
        self._cart = []
        self._cart.append(Item(guid=1234, quantity=2))
        self._shipping_address = Address(
            name='John Doe',
            address='123 Street',
            city='Springfield',
            state='MO',
            zipcode=65807,
        )
        self._billing_information = BillingInformation(
            billing_address=self._shipping_address,
            credit_card_number='1234567890123456',
            expiration_month=12,
            expiration_year=2022,
            card_holder_name='John P. Doe',
        )
        
    def build(self):
        return Order(
            cart=self._cart, 
            billing_information=self._billing_information,
            shipping_address=self._shipping_address,
        )
    
    def with_credit_card_number(self, credit_card_number):
        self._billing_information.credit_card_number = credit_card_number
        return self

    def with_credit_card_expiration_date(self, year, month):
        self._billing_information.expiration_month = month
        self._billing_information.expiration_year = year
        return self


def test_basic(self):
    # Arrange
    order = OrderBuilder().build()
    
    # Act
    #order.checkout()

    # Assert
    #assert order.is_processed == True
        
def test_invalid_order(self):
    order = OrderBuilder() \
        .with_credit_card_number('0f0044433223') \
        .with_credit_card_expiration_date(22, 22) 
        .build()
    #...
    
