def fib(n):
	back = 1
	yield back
	current = 2
	yield current
	next = 3
	while True:
		back = current
		current = next
		next = back + current
		yield current
		if next >= n:
			break

print(sum(i for i in fib(4000000) if i % 2 == 0))