def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        try:
            return n*factorial(n-1)
        except:
            return n