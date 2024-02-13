from yogi import read

n=read(int)

h=(n//3600)
m=(n%3600)//60
s=n%60

print(h,m,s)