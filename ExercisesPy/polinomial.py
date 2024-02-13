from yogi import tokens, read

n = read(float)
result = 0
degree = 0

x = 1
coefficients = []
for c in tokens(float):
    coefficients.append(c)

coefficients.reverse()

for co in coefficients:
    result = result + co*x
    x = x*n

print("{:.4f}".format(result))