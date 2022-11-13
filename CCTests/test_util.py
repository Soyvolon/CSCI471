import unittest
from util import Util

class TestSumNumbers(unittest.TestCase):
    def test_less_than_zero(self):
        # I also don't know the intended result here,
        # if negative numbers were supposed to be added or not.
        assert Util.sum_numbers(-4) == 0

    def test_zero(self):
        assert Util.sum_numbers(0) == 0

    # without knowing what the final intent of this
    # method is, we can't quite test it correctly.
    # Summing non-inclusively may be the intent, 
    # so a case for both inclusive and non-inclusive
    # has been provided.
    def test_greater_than_zero_exclusive(self):
        # 0 + 1 + 2 + 3 = 6
        res = Util.sum_numbers(4)
        assert res == 6

    # def test_greater_than_zero_inclusive(self):
    #     # 0 + 1 + 2 + 3 + 4 = 10
    #     res = Util.sum_numbers(4)
    #     assert res == 10

class TestLeapYear(unittest.TestCase):
    def test_not_400_divide(self):
        res = Util.leap_year(1551)
        assert res == "not a leap year"
        
    def test_400_and_100_divide(self):
        res = Util.leap_year(4000)
        assert res == "leap year"

    def test_400_not_100_divide(self):
        res = Util.leap_year(4444)
        assert res == "leap year"

    def test_4_not_divide(self):
        res = Util.leap_year(1135)
        assert res == "not a leap year"

class TestFindLargest(unittest.TestCase):
    def test_a_less_than_b(self):
        res = Util.find_largest(1,2,3)
        assert res == 3

    def test_a_greater_than_b_less_than_c(self):
        res = Util.find_largest(2,1,3)
        assert res == 3

    def test_a_greater_than_c(self):
        res = Util.find_largest(3,2,1)
        assert res == 3