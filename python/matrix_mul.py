class Solution(object):
	def matrix_mul(self, A, B):
		if len(A[0]) != len(B):
			return None
		res = [[0 for _ in range(len(A))] for _ in range(len(B))]
		for i in range(len(A[0])):
			for j in range(len(B[0])):
				for k in range(len(B)):
					res[i][j] += A[i][k] * B[k][j]
		return res

sl = Solution()
A = [[1,2],[3,4]]
B = [[1,2],[3,4]]
print sl.matrix_mul(A, B)