import unittest
from . import calculator


class TestCacl(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5, "")

    def test_sub(self):
        self.assertEqual(calculator.sub(3, 2), 1)


if __name__ == '__main__':
    unittest.main()
