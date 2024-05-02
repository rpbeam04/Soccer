import unittest

class Test(unittest.TestCase):
    def hello_world(self):
        self.assertEqual(1, 1)

loader = unittest.TestLoader()
suite = loader.discover(__file__)

# Run the suite
runner = unittest.TextTestRunner()
runner.run(suite)