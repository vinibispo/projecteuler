d = 1
c = 0
from datetime import datetime
for y in range(1901, 2001):
  for m in range(1, 13):
    if datetime(y, m, d).weekday() == 6:
      c += 1
print(c)
