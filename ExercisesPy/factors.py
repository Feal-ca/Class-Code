from yogi import read
a = read(int)
b=2
while a>=b:
    if a%b==0:
        print(b)
        a = a//b
        #print("B--> "+str(b))
    else:
        b=b+1
    