"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random
arr = [random.randint(0, 5) for i in range(10)]
counter = {}

for i in arr:
	if i not in counter.keys():
		counter[i] = 1
	else:
		counter[i] += 1

max_ = None
for key in counter.keys():
	if not max_:
		max_ = key
	if counter[key] > counter[max_]:
		max_ = key

print(f'arr: {arr}')
print(f'counter: {counter}')
print(f'max: {max_}')

