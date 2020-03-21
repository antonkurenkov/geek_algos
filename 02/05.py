"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random
arr = [random.randint(-100, 100) for i in range(30)]

max_ = None
for i in range(len(arr)):
	if arr[i] < 0:
		if not max_:
			max_ = i
		if arr[i] > arr[max_]:
			max_ = i

print(arr)
print(max_, arr[max_])
