from nose2.tools import such
from state_gof import *


class MockTurnstile:

    def __init__(self):
        self.actions = []

    def unlock(self):
        self.actions.append('U')

    def raise_alarm(self):
        self.actions.append('A')

    def display(self, message):
        self.actions.append(message)

    def lock(self):
        self.actions.append('L')


with such.A("Turnstile class") as it:

    with it.having("a locked state"):

        @it.has_test_setup
        def setup():
            it.mq_turnstile = MockTurnstile()
            it.turnstile_fsm = TurnstileFSM(it.mq_turnstile)

        with it.having("a coin inserted"):

            @it.has_test_setup
            def setup():
                it.turnstile_fsm.coin()

            @it.should("unlock a gate")
            def test(case):
                assert it.mq_turnstile.actions[-1] == 'U'

            @it.should("change state to unlock")
            def test(case):
                assert it.turnstile_fsm.state == 'UNLOCKED'

        with it.having("a gate passed"):

            @it.has_test_setup
            def setup():
                it.turnstile_fsm.pass_gate()

            @it.should("raise the alarm")
            def test(case):
                assert it.mq_turnstile.actions[-1] == 'A'

            @it.should("keep the state as locked")
            def test(case):
                assert it.turnstile_fsm.state == 'LOCKED'

    with it.having("an unlocked state"):

        @it.has_test_setup
        def setup():
            it.mq_turnstile = MockTurnstile()
            it.turnstile_fsm = TurnstileFSM(it.mq_turnstile)
            it.turnstile_fsm.coin()
            it.mq_turnstile.actions.clear()

        with it.having("a coin inserted"):

            @it.has_test_setup
            def setup():
                it.turnstile_fsm.coin()

            @it.should("display thank you")
            def test(case):
                assert it.mq_turnstile.actions[-1] == 'Thank you...'

            @it.should("keep the state as unlocked")
            def test(case):
                assert it.turnstile_fsm.state == 'UNLOCKED'

        with it.having("a gate passed"):

            @it.has_test_setup
            def setup():
                it.turnstile_fsm.pass_gate()

            @it.should("close a gate")
            def test(case):
                assert it.mq_turnstile.actions[-1] == 'L'

            @it.should("change state to locked")
            def test(case):
                assert it.turnstile_fsm.state == 'LOCKED'

    it.createTests(globals())
