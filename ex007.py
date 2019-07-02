def primes(n):
	ps, cur = [2], 3
	yield 2
	while True:
		y = int(math.sqrt(cur))
		c = next((x for x in ps if x < y and (cur % x) == 0), None)

		if c == None:
			yield cur
			ps.append(cur)

		cur += 2
        if n == 10002:
            break
PrimeList(10001)
