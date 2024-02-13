def reversed(n: int)->int:
    rev = 0
    while n>0:
        digit = (n%10)
        rev = (rev*10)+digit
        n = n//10
    return rev

def is_palindromic(n: int)-> bool:
    """
    Devuelve cierto si el numer es palindromo
    """
    if reversed(n)==n:
        return True
    return False


if __name__ == "__main__":
    print(is_palindromic(12321))
