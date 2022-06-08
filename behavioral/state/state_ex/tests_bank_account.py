from ast import AugAssign
from nose2.tools import such
import pytest
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

        with it.having("a withdraw - amount smaller than balance"):
            @it.has_test_setup
            def setup():
                it.account.withdraw(200.0)

            @it.should("update the balance")
            def test(case):
                assert it.account.balance == 800.0

            @it.should("keep the state as normal")
            def test(case):
                assert it.account.state_description == "Normal"

        with it.having("a withdraw - amount larger than balance"):
            @it.has_test_setup
            def setup():
                it.account.withdraw(1200.0)

            @it.should("update the balance")
            def test(case):
                assert it.account.balance == -200.0

            @it.should("keep the state as overdraft")
            def test(case):
                assert it.account.state_description == "Overdraft"

    with it.having("a overdraft state (balance<=0)"):

        @it.has_test_setup
        def setup():
            it.account = BankAccount(1, -200.0)
            assert it.account.state_description == "Overdraft"                        

        with it.having("a deposit - amount larger than debit"):

            @it.has_test_setup
            def setup():
                it.account.deposit(300.0)
            
            @it.should("change the state to normal")
            def test(case):
                assert it.account.state_description == "Normal"

        with it.having("a withdraw"):
            @it.should("throw InsuffcientFunds exception")
            def test(case):
                with pytest.raises(InsufficientFunds):
                    it.account.withdraw(200)
                

it.createTests(globals())