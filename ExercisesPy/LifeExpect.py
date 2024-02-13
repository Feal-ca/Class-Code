from yogi import read, tokens

y1 = read(int)
y2 = read(int)

max_a = 0.0
max_b = 0.0
dif = []

for c in tokens(str):
    a = read(float)
    b = read(float)
    if a > max_a:
        max_a = a
        c1 = c
    if b > max_b:
        max_b = b
        c2 = c
    dif.append((c,b-a))

dif.sort(reverse=True, key = lambda t: t[1])

print(f"{c1} has the best life expectancy of {y1}.")
print(f"{c2} has the best life expectancy of {y2}.")
print(f"{dif[0][0]} has the best improvement.")
