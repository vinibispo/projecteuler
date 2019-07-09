def collatz_sequence(n):
    c = 0
    while n > 1:
        c += 1
        if n % 2 == 0:
            n /= 2
        else:
            n += 2 * n + 1
    return c
n = 10 ** 6
largest = 0
for i in range(1, n + 1):
    c = collatz_sequence(i)
    if c > largest:
        largest = c
        print(largest)
print(largest)