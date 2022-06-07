import abc

class Component(abc.ABC):
    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent.operation()")


class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, new_component):
        self._component = new_component

    def operation(self):
        self._component.operation()


class ConcreteDecoratorA(Decorator):
    def __init__(self, component, state):
        super().__init__(component)
        self.state = state

    def operation(self):
        Decorator.operation(self)
        print(" + is decorated with a %s" % self.state)


class ConcreteDecoratorB(Decorator):
    def __init__(self, component):
        super().__init__(component)

    def additional_behaviour(self):
        return "additional behaviour"

    def operation(self):
        Decorator.operation(self)
        print(" + is decorated with {}", self.additional_behaviour())


class Client:
    def use(self, component: Component):
        component.operation()


def main():
    component = ConcreteComponent()

    decorated_component = ConcreteDecoratorA(component, "stateA")
    decorated_component = ConcreteDecoratorA(decorated_component, "stateB")
    decorated_component = ConcreteDecoratorB(decorated_component)

    client = Client()
    client.use(decorated_component)

    print("-" * 40)

    decorated_component.component = component
    client.use(decorated_component)

    print("-" * 40)

    decorated_component = ConcreteDecoratorB(
        ConcreteDecoratorA(ConcreteComponent(), "additional state"))
    client.use(decorated_component)


if __name__ == '__main__':
    main()
