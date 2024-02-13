from yogi import read, tokens

first = ""
second = ""
"""
if first < second:
    first, second = second, first
"""
for w in tokens(str):
    if w == first or w == second:
        pass
    elif w > second:
        if w > first:
            second = first
            first = w
        else:
            second = w

print(second)
