def factorial(n):
    if n == 0:
        return 1
    i=n-1
    while i>1:
        n = n*i
        i = i-1
    return n
