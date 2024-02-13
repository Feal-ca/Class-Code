t=int(input())

if t<10:
    message="it's cold"
    if t<=0:
        print("water would freeze")
elif t>30:
    message="it's hot"
    if t>=100:
        print("water would boil")
else:
    message="it's ok"

print(message)

