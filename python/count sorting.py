def counting_sort(A,k):
	b = [0] * (len(A)+1)
	c = [0] * (k + 1)
	for j in range(0, len(A)):
		c[A[j]] += 1
	for i in range(1, k + 1):
		c[i] += c[i-1]
	for j in range(len(A)-1, -1, -1):
		b[c[A[j]]] = A[j]
		c[A[j]] -= 1
	return b[1:]
print counting_sort([2,3,5,0,2,3,0,3], 5)

