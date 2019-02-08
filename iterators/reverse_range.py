# iterator: requires, __iter__ and __next__
#iterable: anything which can be userd in for <item> in <iterable=list>
# Writing a custom iterator using a class way
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

# Writing a custom iterator using a yield, def way
def yield_reverse(start, end):
	while start >= end:
		# yield maintains the previous state of the variable, in this case, each time yield_reverse is called, it suspends 
		# the execution of yield_reverse and returns "start" at statement "yield start" value and when yield_reverse is called again,
		# the execution continues right after the "yield start" statement which is "start -= 1",
		# with "start" value at its previous state maintained
		# but to create an iterator using yield next() on the created iterator must be used to continue execution
		# eg. ite = yield_reverse(10, 1)
		# next(ite) -- 10
		# next(ite) -- 9
		# next(ite) -- 8
		# next(ite) -- 7
		yield start
		start -= 1