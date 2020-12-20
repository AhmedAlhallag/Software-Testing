import unittest
import Ex_1_Calculator.Calculator as Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Happy path testing --> getting the actual value (LHS) to be the same as the expected (RHS)
        self.assertEqual(Calculator.add(10, 10), 20)
        self.assertEqual(Calculator.add(10, -1), 9)
        self.assertEqual(Calculator.add(-10, -10), -20)

    def test_sub(self):
        self.assertEqual(Calculator.sub(10, 10), 0)
        self.assertEqual(Calculator.sub(10, -1), 11)
        self.assertEqual(Calculator.sub(-10, -10), 0)

    def test_mul(self):
        self.assertEqual(Calculator.mul(10, 10), 100)
        self.assertEqual(Calculator.mul(10, -1), -10)
        self.assertEqual(Calculator.mul(-10, -10), 100)

    def test_div(self):
        # Happy path tests
        self.assertEqual(Calculator.div(10, 10), 1)
        self.assertEqual(Calculator.div(10, -1), -10)
        self.assertEqual(Calculator.div(-10, -10), 1)
        # Sad path testing: PASS: if the dveveloper has rasie the expectd exception in certain sirtuation
        #
        with self.assertRaises(ZeroDivisionError):  # Sad path testing: PASS
            Calculator.div(100, 0)
