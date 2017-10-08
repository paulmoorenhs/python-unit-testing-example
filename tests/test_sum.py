from maths.arithmetic import sum
import unittest


class SumCalculatesCorrectlyTestSuite(unittest.TestCase):
    '''
    Test that operations performs the calculation correctly
    '''

    def test_positive_values(self):
        self.assertEqual(2, sum(1, 1))

    def test_negative_values(self):
        self.assertEqual(-2, sum(-1, -1))

    def test_postive_and_negative(self):
        self.assertEqual(-3, sum(3, -6))

    def test_identity(self):
        self.assertEqual(4, sum(4, 0))

    def test_reciprocal(self):
        self.assertEqual(0, sum(4, -4))

    def test_commutative(self):
        self.assertEqual(sum(-5, 4), sum(4, -5))
