def gen_triangle():
	i = 0
	while True:
		i += 1
		yield int(i * (i + 1) / 2)


def amount_divisors(n):
	return len(list(i for i in range(1, n + 1) if n % i == 0))

tri = gen_triangle()
triangle = next(tri)
while True:
	triangle = next(tri)
	if amount_divisors(triangle) > 500:
		print(triangle)
		break