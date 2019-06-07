def getBiggestNumberThatIsEvenlyDivisible(limitNumber):
  testNumber = 2
  while True:
    i = 2
    while True:
      if testNumber % i != 0:
        break
      if i == limitNumber:
        return testNumber
      i += 1
    testNumber += 1
    
  
  return True



print(getBiggestNumberThatIsEvenlyDivisible(20))
