from smallbank import SmallBank
import unittest


class SmallBankTest(unittest.TestCase):

    def setUp(self):
        self.b = SmallBank('Iwena Kroka')

    def testInit(self):
        b = SmallBank('Iwena Kroka')
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

    def testInit_amp(self):
        b = SmallBank('Iwena Kroka')
        self.assertEqual(b.get_transactions(), [])
        self.assertTrue(b.is_empty())
        self.assertEqual(b.owner, 'Iwena Kroka')
        self.assertEqual(b.get_balance(), 0)

    def testDeposit_amp(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_transactions(), [10])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 110)
        self.assertEqual(self.b.get_transactions(), [10, 100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.b.deposit(100)
        self.assertEqual(self.b.get_transactions(), [10, 100, 100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 210)

    def testDeposit_numb_zero_2_call_rem_1(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_transactions(), [10])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(0)
        self.assertEqual(self.b.get_balance(), 10)

    def testDeposit_numb_zero_1_call_add_0_call_rem_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(-45829)
        self.assertEqual(self.b.get_balance(), 0)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(0)
        self.b.deposit(100)
        self.assertEqual(self.b.get_transactions(), [100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 100)

    def testWithdraw_numb_zero_1_call_rem_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(0)
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_none_1_call_add_1_call_rem_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(-55041)
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_call_rem_0(self):
        self.b.withdraw(30)
        self.assertEqual(self.b.get_transactions(), [])
        self.assertTrue(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 0)


if __name__ == '__main__':
    unittest.main()
