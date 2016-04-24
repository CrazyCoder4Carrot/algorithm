def insert_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >=0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

arr = map(int, raw_input().split())
insert_sort(arr)
print arr