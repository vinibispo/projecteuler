def is_prime(n):
    if n == 2:
        return True
    elif n == 0 or n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                prime = True
        return prime


print(sum(list(i for i in range(2, 2 * 10 ** 6) if is_prime(i))))
