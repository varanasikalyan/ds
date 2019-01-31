class CRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		else:
			current = self.value
			self.index += 1
			self.value += 1
			return current

def c_range(start, end):
	while start < end:
		yield start
		start += 1

def c_range_endless(start):
	while True:
		yield start
		start += 1

nums = CRange(1, 10)

g_nums = c_range(1, 10)

g_e_nums = c_range_endless(1)

for num in g_nums:
	print(num)

print(next(g_e_nums))
print(next(g_e_nums))
print(next(g_e_nums))
print(next(g_e_nums))
print(next(g_e_nums))

while True:
	try:
		print(next(nums))
	except StopIteration:
		break
