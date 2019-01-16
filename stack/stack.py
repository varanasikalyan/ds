class Stack():	
	def __init__(self):
		self.items = []
		self.pointer = 0

	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		self.items.pop()

	def display(self):
		print(self.items)