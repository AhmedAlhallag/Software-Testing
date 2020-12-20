import unittest

import Ex_2_TDD_FizzBuzz.fizzbuzz as fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def checkValWithExpected(self, val, expected):
        ret = fizzbuzz.fizz_buzz(val)
        self.assertEqual(ret, expected)

    def test_callFizBuzzReturns1WhenPassed1(self):
        self.checkValWithExpected(1, "1")

    def test_callFizBuzzReturns2WhenPassed2(self):
        self.checkValWithExpected(2, "2")

    def test_callFizBuzzReturnsFizzWhenPassed3(self):
        self.checkValWithExpected(3, "Fizz")

    def test_callFizBuzzReturnsBuzzWhenPassed5(self):
        self.checkValWithExpected(5, "Buzz")

    def test_callFizBuzzReturnsFizzWhenPassedMultipleOf3(self):
        self.checkValWithExpected(6, "Fizz")

    def test_callFizBuzzReturnsBuzzWhenPassedMultipleOf5(self):
        self.checkValWithExpected(10, "Buzz")

    def test_callFizBuzzReturnsFizzBuzzWhenPassed15(self):
        self.checkValWithExpected(15, "FizzBuzz")
