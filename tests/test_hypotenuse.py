from maths.trig import hypotenuse

import math
import unittest


class HypotenuseCalculatesCorrectlyTestSuite(unittest.TestCase):

    def test_is_the_sqaure_root_of_the_sum_of_the_squares_of_the_sides(self):
        self.assertEqual(math.sqrt(4**2 + 5**2), hypotenuse(4, 5))
