import os
import sys
import unittest

# Ensure project root is on sys.path so we can import `src.simple_app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import simple_app as app


class TestSimpleApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(1, 2), 3)
        self.assertEqual(app.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(app.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(app.mul(3, 4), 12)

    def test_div(self):
        self.assertAlmostEqual(app.div(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            app.div(1, 0)


if __name__ == "__main__":
    unittest.main()
