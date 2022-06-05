# Singleton z użyciem metaklasy

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("Singleton.__call__({}, {}, {})".format(cls.__name__, args, kwargs))
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Highlander(metaclass=Singleton):

    def __init__(self, value):
        print('Highlander.__init__({}, {})'.format(self, value))
        self.value = value

    def do_stuff(self):
        print("Highlander.do_stuff(self: {}) with value={}".format(self, self.value))


class Yeti(Highlander):

    def __init__(self, value, footsize):
        super().__init__(value)
        self.footsize = footsize
        print('Yeti.__init__({}, {}, {})'.format(self, value, footsize))

    def do_stuff(self):
        print("Yeti.do_stuff(self: {}) with value={} and footsize={}".format(self, self.value, self.footsize))


def main():

    h1 = Highlander(10)
    h2 = Highlander(30)
    h1.value = 13
    h1.data = 'Test'
    h2.do_stuff()
    print("h2.data={}".format(h2.data))

    print("*"*40)

    y1 = Yeti(80, 102)
    y2 = Yeti(90, 200)

    y1.do_stuff()
    y1.footsize = 300
    y2.do_stuff()

if __name__ == '__main__':
    main()


