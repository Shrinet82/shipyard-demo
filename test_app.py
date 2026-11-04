import unittest

import app


class RenderTest(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("Hello", app.render())


if __name__ == "__main__":
    unittest.main()
