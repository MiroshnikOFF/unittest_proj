import unittest
import utils.arrs

class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(utils.arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(utils.arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(utils.arrs.get([1, 2, 3], -2, "test"), "test")

    def test_slice(self):
        self.assertEqual(utils.arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(utils.arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(utils.arrs.my_slice([], 2, 4), [])
        self.assertEqual(utils.arrs.my_slice([1, 2, 3, 4], -2, 3), [3])
        self.assertEqual(utils.arrs.my_slice([1, 2, 3, 4], -5, 3), [1, 2, 3])