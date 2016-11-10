
import unittest
from main import hello

class TestMain(unittest.TestCase):
	def test_main(self):
		h = hello()
		self.assertEqual(h,"hello")


if __name__ == '__main__':
	unittest.main()
