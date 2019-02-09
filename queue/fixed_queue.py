from iterators.reverse_range import *

class FixedQueue:	
	def __init__(self, cap):
		self.items = [None] * cap
		self.last = -1
		self.first = 0
		self.cap = cap

	def enqueue(self, item):
		if self.last == self.cap - 1:
			return "Unable to push as the Queue is full"
		else:
			self.last += 1
			self.items[self.last] = item
			return item
		
	def dequeue(self):
		if self.first == self.last:
			return "Unable to dequeue as the Queue is empty"
		else:
			ret = self.items[self.first]
			self.items[self.first] = None
			self.first += 1
			return ret

	def is_empty(self):
		return self.items == []

	def display_forward(self):		
		for item in range(self.first, self.last + 1):
			print(self.items[item])

	def display_reverse(self):
		for item in ReverseRange(self.last, self.first):
			print(self.items[item])