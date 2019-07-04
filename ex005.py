def getSmallestNumberThatIsEvenlyDivisible(initialNumber,limitNumber):
  a = initialNumber
  b = 2
  while True:
    b = mmc(a, b)
    a += 1
    if a == limitNumber:
      return b

def mmc(a, b):
  c = a
  d = b
  resto = None
  while resto is not 0:
    resto = c % d
    c = d
    d = resto
  return int(a*b/c)
print(getSmallestNumberThatIsEvenlyDivisible(1, 20))
