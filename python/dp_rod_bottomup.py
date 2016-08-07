import sys
def memoized_cut_rod(p, n):
	r = [0] * n
	for i in range(len(n)):
		r[i] = -sys.maxint
	return memoized_cut_rod_aux(p, n, r)
def memoized_cut_rod_aux(p, n, r):
	if r[n]	 >= 0:
		return r[n]
	if n == 0:
		q = 0
	else :
		q = -sys.maxint
		for i in range(1, n+1):
			q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
	r[n] = q
	return q
def bottom_up_cut_rod(p, n):
	r = [0] * n
	r[0] = 0
	for j in range(1, n+1):
		q = -sys.maxint
		for i in range(1, j+1):
			q = max(q, p[i] + r[j-i])
		r[j] = q
	return r[n]
def extend_bottom_up_cut_rod(p, n):
	r = [0] * n
	s = [0] * n
	r[0] = 0
	for j in range(1, n+1):
		q = - sys.maxint
		for i in range(1, j+1):
			if q < p[i]+r[j-i]:
				q = p[i]+r[j-i]
				s[j] = j
		r[j] = q
	return r, s

def print_cut_rob(p, n):
	r, s = extend_bottom_up_cut_rod(p, n)
	while n > 0:
		print s[n]
		n -= s[n]