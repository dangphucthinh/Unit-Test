import numpy as np 
 
class SimpleStack:
	def Clear(self):
		raise NotImplementedError()
	def Contains(self, value):
		raise NotImplementedError()
	def Peek(self):
		raise NotImplementedError()
	def Push(self, value, capacity):
		raise NotImplementedError()
	def Pop(self):
		raise NotImplementedError()
	def IsEmpty(self):
		raise NotImplementedError()

class StackEmptyException(Exception):
	pass

class IStack(SimpleStack):
	global top
	def __init__(self):
		self.stack=[]
		self.top = -1
		
	def Clear(self):
		self.stack.clear()

	def Contains(self, value):
		if value in np.asarray(self.stack):
			return True
			#print("Found")
		else:
			return False
			#print("Not Found")		

	def Peek(self):
		if self.isEmpty():
			raise StackEmptyException()
		else:
			return self.stack[self.top]

	def isFull(self, capacity):
		if self.top > capacity-1:
			return True
		else:
			return False


	def Push(self, value, capacity):
		if self.isFull(capacity) == True:
			raise TypeError("Stack is full.")
		else:
			self.stack.append(value)

	def Pop(self):
		if self.isEmpty():
			raise StackEmptyException()
		else:
			tmp = self.stack[self.top]
			del self.stack[self.top]	
			return tmp

	def isEmpty(self):
		if len(self.stack)==0:
			return True
		else:
			return False

if __name__ == '__main__':
	k = IStack()