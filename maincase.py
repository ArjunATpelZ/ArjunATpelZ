import unittest
import main


class TestCalc(unittest.TestCase):
    def test_one(self):
        result = main.even(2)
        self.assertEqual(result, 2)

    def test_two(self):
        result = main.even(5101)
        self.assertEqual(result, 5101)



if __name__ == '__main__':
    unittest.main()
