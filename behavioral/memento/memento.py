from copy import copy, deepcopy


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    """Transaction guard"""

    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for state in self.states:
            state()


class Transactional:
    """Adds transactional semantics to methods. Methods decorated with @Transactional will rollback to entry-state
       upon exception"""

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):

        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '1111'
        self.increment()


def main():
    num_obj = NumObj(-1)
    print(num_obj)

    a_transaction = Transaction(True, num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        a_transaction.commit()
        print('--- committed')
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x' # will fail
    except Exception as e:
        a_transaction.rollback()
        print('--- rolled back')
    print(num_obj)

    print('-- now doing stuff ...')
    try:
        num_obj.do_stuff()
    except Exception as e:
        print('-> doing stuff failed!')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)


if __name__ == '__main__':
    main()
