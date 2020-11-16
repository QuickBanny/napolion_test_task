import unittest
from main import Solution


class SolutionTestCase(unittest.TestCase):
    def test_convert(self):
        s = Solution()
        convert = s.roman_to_int
        self.assertEqual(convert('III'), 3)
        self.assertEqual(convert('IV'), 4)
        self.assertEqual(convert('IX'), 9)
        self.assertEqual(convert('LVIII'), 58)
        self.assertEqual(convert('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
