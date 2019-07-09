def d(n):
    return sum(i for i in range(1, n) if n % i == 0)
s = set()
for i in range(1, 10001):
    a = d(i)
    if a != i:
        if i == d(a):
            s.add(i)
            s.add(a)
print(sum(s))