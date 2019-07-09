from num2words import num2words
count = sum(len(str(num2words(i)).replace(' ', '').replace('-', '')) for i in range(1, 1001))
print(count)
