class FixedQueue():	
	def __init__(self, cap):
		self.items = [None] * cap
		self.front = 0
		self.back = 0
		self.cap = cap

	def enqueue(self, item):
		if self.pointer == self.cap:
			return "Unable to push as the Queue is full"
		else:
			self.items[self.pointer] = item
			self.pointer += 1
			return item
		
	def dequeue(self):
		if self.pointer == 0:
			return "Unable to pop as the Queue is empty"
		else:
			self.pointer -= 1
			ret = self.items[self.pointer]
			self.items[self.pointer] = None
			return ret

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[self.pointer - 1]

	def display_forward(self):		
		for item in range(self.back, self.front):
			print(self.items[item])

	def display_reverse(self):
		for item in range(self.back, self.front):
			print(self.items[item])