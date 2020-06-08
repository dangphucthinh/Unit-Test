import unittest
from IStack import IStack, StackEmptyException

class Test_TestStack(unittest.TestCase):
	def setUp(self):
		self.test_stack = IStack()

	def test_push_error(self):
		with self.assertRaises(TypeError):
			self.test_stack.Push(5)

	def test_push_done(self):
		self.test_stack.Push('thinh',3)
		self.assertEqual(self.test_stack.Peek(),'thinh', 'Push error')

	def test_pop_error(self):
		with self.assertRaises(StackEmptyException):
			self.test_stack.Pop()

	def test_pop_done(self):
		self.test_stack.Push('thinh',3)
		self.assertEqual(self.test_stack.Pop(),'thinh', 'Wrong value')
		self.assertTrue(self.test_stack.isEmpty(), 'Pop error')	

	def test_peek_empty(self):
		with self.assertRaises(StackEmptyException):
			self.test_stack.Peek()

	def test_peek_not_empty(self):
		self.test_stack.Push('thinh',3)
		self.assertEqual(self.test_stack.Peek(),'thinh', 'Push error')
		self.assertFalse(self.test_stack.isEmpty(), 'Pop error')	

	def test_contain(self):
		self.test_stack.Push('abc',5)
		self.assertTrue(self.test_stack.Contains('abc'), 'Must be true')	

	def test_not_contain(self):
		self.test_stack.Push('thinh', 5)
		self.assertFalse(self.test_stack.Contains('hnint'), 'Must be false')


	def test_clean(self):
		self.test_stack.Clear()	
		self.assertTrue(self.test_stack.isEmpty(),'Clean error')

	def test_isEmpty(self):
		self.assertTrue(self.test_stack.isEmpty(), 'Not empty')	

	def test_isFull(self):
		self.test_stack.Push('thinh',5)
		self.assertFalse(self.test_stack.isFull(3), 'Full')

if __name__ == '__main__':
	unittest.main()