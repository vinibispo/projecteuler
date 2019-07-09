from math import factorial

def pathfinder(up, right):
  total = up + right
  value = int(factorial(total)/(factorial(up) * factorial(right)))
  return value

print(pathfinder(20, 20))
