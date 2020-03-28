def evens(arr):
	"""
	Наиболее медленный вариант через генератор
	"""
	return [arr.index(item) for item in arr if not item % 2]
	
# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens(list(range(10)))"
# 1000 loops, best of 5: 2.67 usec per loop

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens(list(range(100)))"
# 1000 loops, best of 5: 51.1 usec per loop

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens(list(range(1000)))"
# 1000 loops, best of 5: 3.88 msec per loop

def evens2(arr):
	"""
	Наиболее быстрый вариант через цикл
	"""
	even = []
	for item in arr:
		if not item % 2:
			even.append(item)
	return even

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens2(list(range(10)))"
# 1000 loops, best of 5: 1.68 usec per loop

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens2(list(range(100)))"
# 1000 loops, best of 5: 9.42 usec per loop

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens2(list(range(1000)))"
#1000 loops, best of 5: 99.4 usec per loop

def evens3(arr):
	"""
	Средний по скорости вариант через фильтр
	"""
	return list(filter(lambda x: not x % 2, arr))

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens3(list(range(10)))"
# 1000 loops, best of 5: 2.65 usec per loop

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens3(list(range(100)))"
# 1000 loops, best of 5: 15.6 usec per loop

# python3 -m timeit -n 1000 -s "import task_02" "task_02.evens3(list(range(1000)))"
# 1000 loops, best of 5: 156 usec per loop