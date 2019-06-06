def palindrome(n):
    for i in range(10 ** (n-1), 10 ** n):
        for j in range(10 ** (n-1), 10 ** n):
            s = str(i * j)
            # if (s[0:n] == s[n:-1]):
            #     print(s)
            print(s)

palindrome(2)