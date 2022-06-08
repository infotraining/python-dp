import abc


class TurnstileAPI:

    def lock(self):
        print("Lock...")

    def unlock(self):
        print("Unlock...")

    def raise_alarm(self):
        print("Alarm...")

    def display(self, message):
        print(message)


class TurnstileFSM_Before:

    def __init__(self, turnstile_api):
        self.turnstile_api = turnstile_api
        self.state = 'LOCKED'

    def coin(self):
        if self.state == 'LOCKED':
            self.turnstile_api.unlock()
            self.state = 'UNLOCKED'
        elif self.state == 'UNLOCKED':
            self.turnstile_api.display('Thank you...')

    def pass_gate(self):
        if self.state == 'LOCKED':
            self.turnstile_api.raise_alarm()
        elif self.state == 'UNLOCKED':
            self.turnstile_api.lock()
            self.state = 'LOCKED'


class TurnstileState(abc.ABC):
    @abc.abstractmethod
    def coin(self, turnstile_api):
        pass

    @abc.abstractmethod
    def pass_gate(self, turnstile_api):
        pass

    @abc.abstractproperty
    def name(self):
        pass

class LockedState(TurnstileState):

    def coin(self, turnstile_api):
        turnstile_api.unlock()
        return unlocked_state

    def pass_gate(self, turnstile_api):
        turnstile_api.raise_alarm()
        return self

    @property
    def name(self):
        return 'LOCKED'


class UnlockedState(TurnstileState):

    def coin(self, turnstile_api):
        turnstile_api.display("Thank you...")
        return self

    def pass_gate(self, turnstile_api):
        turnstile_api.lock()
        return locked_state

    @property
    def name(self):
        return 'UNLOCKED'

# singleton states
locked_state = LockedState()
unlocked_state = UnlockedState()


class TurnstileFSM_After:

    def __init__(self, turnstile_api):
        self.turnstile_api = turnstile_api
        self.__state = LockedState()

    def coin(self):
        self.__state = self.__state.coin(self.turnstile_api)

    def pass_gate(self):
        self.__state = self.__state.pass_gate(self.turnstile_api)

    @property
    def state(self):
        return self.__state.name


TurnstileFSM = TurnstileFSM_After


def main():

    turnstile = TurnstileFSM(TurnstileAPI())

    turnstile.coin()
    turnstile.pass_gate()
    turnstile.pass_gate()
    turnstile.coin()
    turnstile.pass_gate()
    turnstile.coin()
    turnstile.coin()
    turnstile.coin()
    turnstile.coin()

if __name__ == '__main__':
    main()