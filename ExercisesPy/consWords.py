from yogi import tokens, read

firstWord = read(str)
consecutive = 1
prevWord = firstWord
maxCons = 1
for w in tokens(str):
    if w == prevWord == firstWord:
        consecutive = consecutive + 1
        if consecutive > maxCons:
            maxCons = consecutive
    elif w == firstWord:
        consecutive = 1
    else:
        consecutive = 0
    prevWord = w
print(maxCons)
