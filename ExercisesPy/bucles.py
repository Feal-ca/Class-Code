from yogi import read
a = read(int)
b = read(int)


while a<b:
    print(str(a)+",",end="")
    a = a+1
if a == b:
    print(str(a))
if a>b:
    print("")