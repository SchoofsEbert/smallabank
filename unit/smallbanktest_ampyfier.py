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

    def testWithdraw_amp(self):
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 100)
        self.assertEqual(self.b.get_transactions(), [100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.b.withdraw(30)
        self.assertEqual(self.b.get_transactions(), [100, -30])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 70)

    def testWithdraw_numb_zero_1_call_rem_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only withdraw an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_numb_zero_0_call_rem_1(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_numb_zero_0_call_add_1_none_1(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(-32130)
        self.assertEqual(excep_info.exception.args, (
            'Can only withdraw an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_call_rem_0(self):
        self.b.withdraw(30)
        self.assertEqual(self.b.get_transactions(), [])
        self.assertTrue(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_call_add_0_none_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(-49238)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        self.b.withdraw(30)
        self.assertEqual(self.b.get_transactions(), [])
        self.assertTrue(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 0)


if __name__ == '__main__':
    unittest.main()
