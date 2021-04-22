import unittest
import tools
from function import cvicenie_a

class FunctionsTestCasse(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(cvicenie_a.is_prime(self, 13), True, "Shoud be True")
        self.assertEqual(cvicenie_a.is_prime(self, 3), True, "Shoud be True")
        self.assertEqual(cvicenie_a.is_prime(self, 14), False, "Shoud be False")
        self.assertEqual(cvicenie_a.is_prime(self, 21), False, "Shoud be False")

    def test_tool(self):
        self.assertEqual(tools.is_prime(13), True, "Shuld be True")
        self.assertEqual(tools.is_prime(3), True, "Shuld be True")
        self.assertEqual(tools.is_prime(14), False, "Shuld be False")
        self.assertEqual(tools.is_prime(21), False, "Shuld be False")
        self.assertEqual(tools.is_prime(52), False, "Shuld be False")


if __name__ == '__main__':
    unittest.main()
