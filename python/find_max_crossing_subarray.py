import sys
class Solution(object):
	def find(self, A, low, high):
		mid = (high + low) / 2
		sum = max_left = max_right = 0
		left_sum = -sys.maxint
		for i in range(low, mid + 1)[::-1]:
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
	def find_max(self, A, low, high):
		if low == high:
			return low, high, A[low]
		else:
			mid = (low + high) / 2
			left_low, left_hight, left_sum = find_max(A, low, mid)
			right_low, right_high, right_sum = find_max(A, mid+1, high)
			cross_low, cross_high, cross_sum = find(A, low, high)
			if left_sum >= right_sum and left_sum >= cross_sum:
				return left_low, left_high, left_sum
			elif right_sum >= left_sum and right_sum >= cross_sum:
				return right_low, right_high, right_sum
			else:
				return cross_low, cross_high, cross_sum

s1 = Solution()
A = [13, -3, -25, 20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4]
print s1.find(A, 0, len(A) - 1)