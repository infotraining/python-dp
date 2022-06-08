from nose2.tools import such
from bank_account import *

with such.A("BankAccount") as it:

    with it.having("an initial state"):

        @it.has_test_setup
        def setup():
            it.account = BankAccount(1)

        @it.should("have balance set to zero")
        def test(case):
            assert it.account.balance == 0.0

        @it.should("return description as normal state")
        def test(case):
            assert it.account.state_description == "Normal"

    with it.having("a normal state (balance>=0)"):

        @it.has_test_setup
        def setup():
            it.account = BankAccount(1, 1000.0)
            assert it.account.balance >= 0

        with it.having("a deposit"):

            @it.has_test_setup
            def setup():
                it.account.deposit(100.0)

            @it.should("add deposited amount to balance")
            def test(case):
                assert it.account.balance == 1100.0

            @it.should("keep the state as normal")
            def test(case):
                assert it.account.state_description == "Normal"



it.createTests(globals())