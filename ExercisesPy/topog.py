from yogi import tokens, read

old_mon = 0
old_neu = 0

for mon in tokens(int):
    neu = read(int)
    mon = old_mon + mon
    neu = old_neu + neu

    if neu < 0 or mon < 0:
        print("ERROR")
        break
    print("X"*mon,end="")
    print("."*neu)

    old_mon = mon
    old_neu = neu