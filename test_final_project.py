import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertAlmostEqual(True, True)


if __name__ == "__main__":
    unittest.main()
