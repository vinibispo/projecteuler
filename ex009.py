from math import sqrt
def pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(1, n):
            c = sqrt(a ** 2 + b ** 2)
            if a + b + c == n:
                return a * b * c


print(pythagorean_triplet(1000))
