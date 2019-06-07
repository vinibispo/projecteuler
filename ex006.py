def sumofSquares(n):
    return sum([i ** 2 for i in range(0, n + 1)])

def squareofSum(n):
    return sum([i for i in range(0, n + 1)]) ** 2


def differenceofSquares(n):
    return squareofSum(n) - sumofSquares(n)

print(differenceofSquares(100))