l  = list()
n = int(input())
def function(l, n):
    l = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]
    return sum(l)
print(function(l, n))
