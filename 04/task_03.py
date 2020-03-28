def sieve(n, max_range=1000):
	"""
	Скорость зависит от диапазона перебираемых чисел
	"""
	try:
	    temp = list(range(max_range))
	    temp[1] = 0
	    for i in temp:
	        if i > 1:
	            for j in range(i + i, len(temp), i):
	                temp[j] = 0
	    return list(filter(lambda x: x, temp))[n-1]
	except IndexError:
		return -1

# python3 -m timeit -n 1000 -s "import task_03" "task_03.sieve(10)"
# 1000 loops, best of 5: 339 usec per loop

# python3 -m timeit -n 1000 -s "import task_03" "task_03.sieve(100)"
# 1000 loops, best of 5: 341 usec per loop

def prime(n, max_range=1000):
	"""
	Скорость зависит от диапазона перебираемых чисел
	"""
	lst=[]
	try:
	    for i in range(2, max_range):
		    for j in lst:
		        if not i % j:
		            break
		    else:
		        lst.append(i)
	    return lst[n-1]
	except IndexError:
		return -1

# python3 -m timeit -n 1000 -s "import task_03" "task_03.prime(1)"
# 1000 loops, best of 5: 966 usec per loop

# python3 -m timeit -n 1000 -s "import task_03" "task_03.prime(100)"
# s1000 loops, best of 5: 980 usec per loop