class quick_sort(object):
	def __init__(self, input):
		self.A = input
	def sort(self):
		self.quicksort(0, len(self.A) - 1)
	def quicksort(self, p, r):
		if p < r:
			q = self.partition(p, r)
			self.quicksort(p, q-1)
			self.quicksort(q+1, r)
	def partition(self, p, r):
		x = self.A[r]
		i = p - 1
		for j in range(p, r):
			if self.A[j] <= x:
				i += 1
				self.A[i], self.A[j] = self.A[j], self.A[i]
		self.A[i + 1], self.A[r] = self.A[r], self.A[i + 1]
		return i + 1

sort = quick_sort([4,2,1,7,8,9])
sort.sort()
print sort.A
