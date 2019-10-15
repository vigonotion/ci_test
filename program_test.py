import unittest
import xmlrunner
from ddt import ddt, data, idata, file_data, unpack

from program import *


@ddt
class TestProgram(unittest.TestCase):
    @data((1, 2, 3), (0, 0, 0), (5, 0, 5), (-5, 7, 2))
    @unpack
    def test_add(self, a, b, x):
        self.assertEqual(add(a, b), x)

    @data((5, 3, 2), (6, 6, 0), (2, 8, -6))
    @unpack
    def test_sub(self, a, b, x):
        self.assertEqual(sub(a, b), x)

    @data((2,5,10),(3,0,0), (-1,-6,6))
    @unpack
    def test_mul(self, a, b, x):
        self.assertEqual(mul(a, b), x)

    @data((6,2,3),(3,2,1.5), (-10,-2,5))
    @unpack
    def test_div(self, a, b, x):
        self.assertEqual(div(a, b), x)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))