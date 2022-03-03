import random

class SmallBank:
    def __init__(self, owner):
        self._balance = 0
        self._transactions = []
        self.owner = owner

    def get_self(self):
        return self

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                self._transactions.append(-amount)
        else:
            raise Exception("Can only withdraw an amount > 0")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(amount)
        else:
            raise Exception("Can only deposit an amount > 0")

    def is_empty(self):
        return self._balance == 0

    def get_random(self):
        return random.random()

    def get_transaction(self, index):
        return self._transactions[index]

    def get_transactions(self):
        return self._transactions
