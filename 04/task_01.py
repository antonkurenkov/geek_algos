def count(n):
	"""
	Наиболее предпочтительный по скорости вариант
	"""
	r = range(1, 10)
	counter = {i:0 for i in r}
	for num in range(2, n):
		for i in r:
			if not num % i:
				counter[i] += 1
	return counter

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count(100)"
# 1000 loops, best of 5: 84.5 usec per loop

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count(1000)"
# 1000 loops, best of 5: 818 usec per loop

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count(10000)"
# 1000 loops, best of 5: 8.48 msec per loop

def count2(n):
	"""
	Медленный и непонятный вариант
	"""
	r = range(1, 10)
	counter = {i:0 for i in r}
	for num in range(2, n):
		for i in r:
			counter[i] += 1 and not num % i
	return counter

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count2(100)"
# 1000 loops, best of 5: 142 usec per loop

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count2(1000)"
# 1000 loops, best of 5: 1.48 msec per loop

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count2(10000)"
# 1000 loops, best of 5: 15.9 msec per loop

def count3(n):
	"""
	Вариант с дополнительной вложенной функцией
	"""

	def count_(num):
		return sum(map(lambda x: not x % num, arr))

	arr = list(range(2, n))
	return {i: count_(i) for i in range(1, 10)}

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count3(100)"
# 1000 loops, best of 5: 132 usec per loop

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count3(1000)"
# 1000 loops, best of 5: 1.33 msec per loop

# python3 -m timeit -n 1000 -s "import task_01" "task_01.count3(10000)"
# 1000 loops, best of 5: 14.6 msec per loop

