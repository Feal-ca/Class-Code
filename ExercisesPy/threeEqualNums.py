from yogi import read

def three_equal_consecutive_digits(n: int, b:int) -> bool:
    """
    Indica si un nombre (n) escrit en base (b) té 3 o més xifres iguals consecutives
    """

    while n>(b*b):
        # Compara les tres últimes xifres
        if n%b == (n//b)%b and (n//b)%b == (n//(b*b))%b:
            return True

        return three_equal_consecutive_digits(n//b, b)

    return False

if __name__ == "__main__":
    n = read(int)
    b = read(int)
    print(three_equal_consecutive_digits(n, b)) # returns bool

