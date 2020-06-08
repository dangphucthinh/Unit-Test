import unittest
from IStack import IStack, StackEmptyException

class Test_TestStack(unittest.TestCase):
	def setUp(self):
		self.test_stack = IStack()

	def test_push(self):
		with self.assertRaises(TypeError):
			self.test_stack.Push(5)

	def test_pop(self):
		with self.assertRaises(StackEmptyException):
			self.test_stack.Pop()

	def test_peek(self):
		with self.assertRaises(StackEmptyException):
			self.test_stack.Peek()

	def test_contain(self):
		self.test_stack.Push('abc',5)
		self.assertTrue(self.test_stack.Contains('abc'), 'Must be true')

if __name__ == '__main__':
	unittest.main()