from yogi import read
while True:
    n=read(int)
    p1=str(n)
    if len(str(p1))==1:
        print(f"The product of the digits of {p1} is {p1}.")
    else:
        while len(str(p1))>1:
            p2 = 1
            for digit in str(p1):
                p2 = p2 * int(digit)
            print(f"The product of the digits of {p1} is {p2}.")
            p1 = p2

    print("----------")
