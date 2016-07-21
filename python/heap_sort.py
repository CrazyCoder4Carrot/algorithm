class heap(object):
	def __init__(self, input):
		self.length = len(input)
		self.A = [0] + input
	def left(self, i):
		return i << 1
	def right(self, i):
		return (i << 1) + 1
	def parent(self, i):
		return i >> 1
	def max_heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		if l <= self.length and self.A[l] > self.A[i]:
			largest = l
		else:
			largest = i
		if r <= self.length and self.A[r] > self.A[largest]:
			largest = r
		if largest != i:
			self.A[i], self.A[largest] = self.A[largest], self.A[i]
			self.max_heapify(largest)
	def build_max_heap(self):
		for i in range(self.length/2, 0, -1):
			self.max_heapify(i)
	def heap_sort(self):
		self.build_max_heap()
		for i in range(self.length, 1, -1):
			self.A[1], self.A[i] = self.A[i], self.A[1]
			self.length -= 1
			self.max_heapify(1)

heap = heap([4,1,3,2,19,9,10,14,8,7])
heap.heap_sort()
print heap.A[1:]

