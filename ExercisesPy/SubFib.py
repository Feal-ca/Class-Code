from yogi import tokens

def is_fib(n: int):
    a1,a2 = 1,2
    a = 0
    if n==1 or n==2:
        return True
    while a<=n:
        a=a1+a2
        a1=a2
        a2=a
        if a == n:
            return True
    return False


def is_fib_sequence()->bool:

    for num in tokens(int):
        if not is_fib(num):
            return False
    return True

if __name__ == "__main__":
    if is_fib_sequence():
        print("yes")
    else:
        print("no")
