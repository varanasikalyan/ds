class Queue:	
	def __init__(self):
		self.items = []
		self.pointer = 0

	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def display(self):
		return self.items