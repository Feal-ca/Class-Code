from yogi import tokens
c = 1
for n in tokens(int):
    if n%2==0:
        print(c)
        break
    else:
        c = c + 1