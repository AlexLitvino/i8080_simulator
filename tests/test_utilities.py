import unittest

from utilities import get_bit

value0 = 0b0
value1 = 0b1
value4 = 0b100
value6 = 0b110


class TestGetBit(unittest.TestCase):

    def test_value0(self):
        self.assertEqual(get_bit(value0, 0), 0b0)
        self.assertEqual(get_bit(value0, 1), 0b0)

    def test_value1(self):
        self.assertEqual(get_bit(value1, 0), 0b1)
        self.assertEqual(get_bit(value1, 1), 0b0)
        self.assertEqual(get_bit(value1, 2), 0b0)

    def test_value4(self):
        self.assertEqual(get_bit(value4, 0), 0b0)
        self.assertEqual(get_bit(value4, 1), 0b0)
        self.assertEqual(get_bit(value4, 2), 0b1)
        self.assertEqual(get_bit(value4, 3), 0b0)

    def test_value6(self):
        self.assertEqual(get_bit(value6, 0), 0b0)
        self.assertEqual(get_bit(value6, 1), 0b1)
        self.assertEqual(get_bit(value6, 2), 0b1)
        self.assertEqual(get_bit(value6, 3), 0b0)


if __name__ == "__main__":
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetBit)
    unittest.TextTestRunner(verbosity=2).run(suite)