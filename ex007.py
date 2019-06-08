def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def PrimeList(n):
    l = list()
    a = 1
    while True:
        a = a + 1
        if isPrime(a):
            l.append(a)
        if len(l) == n:
            break
    print(max(l))

PrimeList(10001)