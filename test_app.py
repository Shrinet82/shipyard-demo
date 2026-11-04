import unittest

import app


class RenderTest(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("Hello", app.render())

    def test_health(self):
        self.assertEqual(app.health(), "ok\n")


if __name__ == "__main__":
    unittest.main()
