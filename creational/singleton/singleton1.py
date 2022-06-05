class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def do_stuff(self):
        print("Singleton.do_stuff(self: {})".format(self))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data


def main():
    s1 = Singleton()
    s1.do_stuff()
    s1.data = 2
    s2 = Singleton()
    print(s1.data)
    s2.do_stuff()


if __name__ == "__main__":
    main()