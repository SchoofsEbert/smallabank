import pytest
from smallbank import SmallBank

import ampyfier

@ampyfier.amplify_ignore
def test_init():
    b = SmallBank("Owner Ownerson")
    assert b.get_balance() == 0

@ampyfier.amplify_selection("NUM")
def test_deposit(monkeypatch):
    b = SmallBank("Owner Ownerson")
    b.deposit(10)
    assert b.get_balance() == 10
    b.deposit(100)
    b.deposit(100)
    assert b.get_balance() == 210


def test_withdraw():
    b = SmallBank("Owner Ownerson")
    b.deposit(100)
    b.withdraw(30)
    assert b.get_balance() == 70


@ampyfier.amplify_ignore
def test_get_transaction():
    b = SmallBank("Owner Ownerson")
    b.deposit(100)
    assert b.get_transaction(0) == 100
