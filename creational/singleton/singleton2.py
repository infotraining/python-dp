def singleton(cls):
    
    def __new__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = object.__new__(cls)
            return cls.__instance
    
    cls.__new__ = staticmethod(__new__)
    return cls


@singleton
class OneOnly:

    def __init__(self):
        pass


def main():
    
    a = OneOnly()
    a.value = 42
    b = OneOnly()

    print("is singleton? {}", id(a) == id(b))

    print(type(a))
    print(type(b))
    print(b.value)

if __name__ == "__main__":
    main()