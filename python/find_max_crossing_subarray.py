import sys
class Solution(object):
	def find(self, A, low, high):
		mid = (high + low) / 2
		sum = max_left = max_right = 0
		left_sum = -sys.maxint
		for i in range(low, mid + 1)[::-1]:
			print i
			sum += A[i]
			if sum > left_sum:
				left_sum = sum
				max_left = i
		right_sum = -sys.maxint
		sum = 0
		for j in range(mid + 1, high):
			sum += A[j]
			if sum > right_sum:
				right_sum = sum
				max_right = j
		return max_left, max_right, left_sum + right_sum

s1 = Solution()
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4]
print s1.find(A, 0, len(A) - 1)