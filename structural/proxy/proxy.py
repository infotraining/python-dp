from functools import cache
from typing import Type


@cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class CacheFunction:
    def __init__(self, f):
        self.__function = f
        self.__cache = {}

    def __call__(self, *args):
        try:
            return self.__cache[args]
        except KeyError:
            result = self.__function(*args)
            self.__cache[args] = result
            return result
        except TypeError: # unhashable object in args
            return self.__function(*args)


def client(f):
    print(f(20, 21))
    print(f(20, 21))

def fib_sum(a, b):
    return fibonacci(a) + fibonacci(b)

if __name__ == "__main__":
    client(CacheFunction(fib_sum))