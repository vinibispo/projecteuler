def palindrome(n):
    l = list()
    for i in range(10 ** (n-1), 10 ** n):
        for j in range(10 ** (n-1), 10 ** n):
            s = str(i * j)
            # 9090
            if s == s[::-1]:
                l.append(i * j)
    return max(l)
print(palindrome(3))
