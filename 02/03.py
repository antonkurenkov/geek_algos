"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
arr = [random.randint(0, 1000) for i in range(30)]

max_ = None
min_ = None
for i in range(len(arr)):
	if not min_ and not max_:
		min_ = i; max_ = i
	if arr[i] < arr[min_]:
		min_ = i
	if arr[i] > arr[max_]:
		max_ = i

print(arr)
arr[min_], arr[max_] = arr[max_], arr[min_]
print(arr)
