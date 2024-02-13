from yogi import tokens, read, scan

def print_sorted_words()->None:
    a = read(str)
    b = read(str)

    while b != "END":
        if a>b:
            print(b)
            a,b = b,a
        else:
            print(a)
        a = b
        b = read(str)
    print(a)

if __name__ == "__main__":
    print_sorted_words()


"""
a
b
e
c
d
f
g
END

b
a
c
END

"""

