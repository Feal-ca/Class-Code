from yogi import read
n = read(int)

# Triangulo 1
for i in range(n):
    for j in range(n-1-i):
        print("_",end="")
    for j in range(2*i+1):
        print("*",end="")
    print("")

# Triangulo 2
for i in range(n-1):
    for j in range(i+1):
        print("_",end="")
    for j in range(2*(n-i-1)-1):
        print("*",end="")
    print("")