from yogi import tokens, read, scan


if __name__ == "__main__":
    a = read(int)
    i = a-1
    x = scan(int)
    while x is not None and i>0:
        i = i-1
        x = scan(int)
    if x is None or a<=0:
        print("Incorrect position.")
    else:
        print(f"At the position {a} there is a(n) {x}.")
