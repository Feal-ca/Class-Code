from yogi import tokens

for n in tokens(int):
    i = 0
    while n != 1:
        if n%2==0:
            n = n//2
        else:
            n = (3*n)+1
        i = i+1
    print(i)