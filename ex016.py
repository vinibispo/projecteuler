def power_digit_sum(base, expoent):
  string = str(base ** expoent)
  return sum(int(i) for i in string)

print(power_digit_sum(2, 1000))
