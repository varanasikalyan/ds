class FixedStack():	
	def __init__(self, cap):
		self.items = [None] * cap
		self.pointer = 0
		self.cap = cap

	def push(self, item):
		if self.pointer == self.cap:
			return "Unable to push as the stack is full"
		else:
			self.items[self.pointer] = item
			self.pointer += 1
			return item
		
	def pop(self):
		if self.pointer == 0:
			return "Unable to pop as the stack is empty"
		else:
			self.pointer -= 1
			ret = self.items[self.pointer]
			self.items[self.pointer] = None
			return ret

	def display(self):
		for item in range(self.pointer):
			print(self.items[item])