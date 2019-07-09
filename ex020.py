from math import factorial

def sum_digits_factorial(n):
  return sum(int(x) for x in str(factorial(n)))

print(sum_digits_factorial(100))
