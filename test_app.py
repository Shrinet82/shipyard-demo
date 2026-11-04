import unittest

import app


class RenderTest(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("Hello", app.render())

    def test_footer_is_v9(self):
        self.assertEqual(app.FOOTER, "v9")


if __name__ == "__main__":
    unittest.main()
