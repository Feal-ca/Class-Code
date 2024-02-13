from yogi import read
a = read(int)
b = read(int)
c = read(int)

n= 3600*a+60*b+c+1
h=(n//3600)%24
m=(n%3600)//60
s=n%60
if h < 10:
    h="0"+str(h)
if m < 10:
    m="0"+str(m)
if s < 10:
    s="0"+str(s)

print(str(h)+":"+str(m)+":"+str(s))