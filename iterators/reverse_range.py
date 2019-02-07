class ReverseRange:
	"""Generates Reverse Range"""
	def __init__(self, start, end):
		if start <= end:
			raise ValueError("end argument cannot be greater than start")
		self.value = start
		self.end = end
		self.index = -1
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.value < self.end:
			raise StopIteration
		else:
			current = self.value
			self.index -= 1
			self.value -= 1
			return current

def yield_reverse(start, end):
	while start >= end:
		yield start
		start -= 1