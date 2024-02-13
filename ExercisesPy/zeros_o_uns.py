def zeros_o_uns(n):
    n = str(bin(n)[2:])
    z = 0
    u = 0
    i=0
    for i in range(0,len(n)):
        if n[i]=="1":
            u = u+1
        else:
            z = z+1
    #print(f"z={z},u={u}")
    if z>u:
        return "0"
    elif u>z:
        return "1"
    else:
        return "2"
