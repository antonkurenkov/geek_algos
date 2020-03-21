"""
1. В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 

Примечание: 8 разных ответов.
"""

r = range(2, 9)
counter = {i:0 for i in r}
for num in range(2, 99):
	for i in r:
		if not num % i:
			counter[i] += 1

print(counter)