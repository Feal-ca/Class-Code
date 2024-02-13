from yogi import read

def avalua() -> int:
    char = read(str)

    if char == "+":
        r1 = avalua()
        r2 = avalua()
        return r1+r2
    if char == "-":
        return str((-1) * int(avalua()))
    if char == "m":
        a = avalua()
        b = avalua()
        c = avalua()

        return max(a,b,c)

    assert char in "0123456789"
    return char

if __name__ == "__main__":
    print(avalua())
