li = list()
def decomposition(n):
    a = n
    c = 0
    for i in range(2, n):
        if a % i == 0:
            a /= i
            for j in range(2,i):
                if i % j == 0:
                    c += 1
            if c == 0:
                li.append(i)
    print(max(li))

decomposition(600851475143)