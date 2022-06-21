from smallbank import SmallBank
import unittest
from flask import jsonify

class SmallBankTest(unittest.TestCase):
    def setUp(self):
        self.b = SmallBank("Iwena Kroka")

    def testInit(self):
        b = SmallBank("Iwena Kroka")
        self.assertEqual(b.get_balance(), 0)

    def testDeposit(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        self.b.deposit(100)
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 210)

    def testWithdraw(self):
        self.b.deposit(100)
        self.b.withdraw(30)
        self.assertEqual(self.b.get_balance(), 70)

    def testGetTransaction(self):
        self.b.deposit(100)
        self.assertEqual(self.b.get_transaction(0), 100)


if __name__ == '__main__':
    unittest.main()
