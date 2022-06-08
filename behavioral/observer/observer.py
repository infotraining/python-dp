import abc


class Subject:
    def __init__(self):
        self._observers = set()

    def register_observer(self, observer):
        self._observers.add(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def _notify(self, event):
        for observer in self._observers:
            observer(self, event)


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._data = 0.0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        if self._data != new_data:
            self._data = new_data
            self._notify(self._data)


class Observer(abc.ABC):

    @abc.abstractmethod
    def __call__(self, sender, event_args):
        pass


class ConcreteObserver(Observer):
    def __init__(self, id):
        self.id = id

    def __call__(self, sender, event_args):
        print("ConcreteObserver({}) is notified by {} - event args: {}".format(self.id, sender, event_args))


def log(sender, event_args):
    print("Logging event {} from {}".format(event_args, sender))


def main():
    cs = ConcreteSubject()
    cs.register_observer(log)

    o1 = ConcreteObserver(1)
    o2 = ConcreteObserver(2)

    cs.register_observer(o1)
    cs.register_observer(o2)

    cs.data = 99.9

    print("*"*40)

    cs.data = 100.2

    cs.unregister_observer(o1)

    print("*"*40)

    cs.data = 102.4


if __name__ == '__main__':
    main()
