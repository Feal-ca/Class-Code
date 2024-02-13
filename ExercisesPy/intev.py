from yogi import read

a1=read(int)
a2=read(int)
b1=read(int)
b2=read(int)

if b1==a1 and b2==a2:
    print("=",end="")
elif a1<=b1 and b2<=a2:
    print("2",end="")
elif b1<=a1 and a2<=b2:
    print("1",end="")
else:
    print("?",end="")
print(" , ",end="")
if b1<=a1 and b2>=a2:
    print("["+str(a1)+","+str(a2)+"]")
elif a1<=b1 and a2>=b2:
    print("["+str(b1)+","+str(b2)+"]")
elif b1<=a2 and b2>=a2:
    print("["+str(b1)+","+str(a2)+"]")
elif b1<=a1 and b2>=a1:
    print("["+str(a1)+","+str(b2)+"]")
else:
    print("[]")
"""
if b1==a1 and b2==a2:
    print("=")
elif a1<=b1 and b2<=a2:
    print("2")
elif b1<=a1 and a2<=b2:
    print("1")
else:
    print("?")
    """