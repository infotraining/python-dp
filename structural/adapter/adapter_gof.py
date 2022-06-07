class Adaptee:
    def specific_request(self):
        print("Adaptee.specific_request()")


class Target:
    def request(self):
        pass


class Client:
    def use(self, target):
        target.request()


# Approach 1
class ObjectAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


# Approach 2
class ClassAdapter(Adaptee):
    def request(self):
        super().specific_request()


# Approach 3 - pythonic way
class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


# Approach 4 - mixin
class AdapterMixin:
    def request(self):
        self.specific_request()


class Adapter2(AdapterMixin, Adaptee):
    pass


def main():

    client = Client()

    print("+ object adapter " + '-' * 10)
    adaptee = Adaptee()
    adapter = ObjectAdapter(adaptee)
    client.use(adapter)

    print("+ class adapter " + '-' * 10)
    client.use(ClassAdapter())

    print("+ pythonic adapter " + '-' * 10)
    client.use(Adapter(adaptee, {"request": adaptee.specific_request}))

    print("+ mixin adapter " + '-' * 10)
    client.use(Adapter2())

    print("+ collection of adapters " + '-' * 10)
    targets = [ObjectAdapter(adaptee), ClassAdapter(),
               Adapter(adaptee, {"request": adaptee.specific_request}), Adapter2()]
    
    for target in targets:  # doctest: +NORMALIZE_WHITESPACE
        client.use(target) 
    

if __name__ == "__main__":
    main()    
