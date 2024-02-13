def isLeap(year):
    if year%100==0:
        if (year//100)%4==0:
            return True
    elif year%4==0:
        return True
    return False
def month_to_num(month):
    if month == "gener":
        return 1
    if month == "febrer":
        return 2
    if month == "marc":
        return 3
    if month == "abril":
        return 4
    if month == "maig":
        return 5
    if month == "juny":
        return 6
    if month == "juliol":
        return 7
    if month == "agost":
        return 8
    if month == "setembre":
        return 9
    if month == "octubre":
        return 10
    if month == "novembre":
        return 11
    if month == "desembre":
        return 12

def dia_seguent(d,m,y):
    months=["gener","febrer","marc","abril","maig","juny","juliol","agost","setembre","octubre","novembre","desembre"]
    m = month_to_num(m)
    
    if isLeap(y) and d==29 and m==2:
        return f"(1, 'marc', {y})"
    
    elif m==12 and d==31:
        return f"(1, 'gener', {y+1})"
    
    elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and d==31:
        return f"(1, '{months[m]}', {y})"
    
    elif (m==4 or m==6 or m==9 or m==11) and d==30:
        return f"(1, '{months[m]}', {y})"
    
    elif m==2 and not isLeap(y) and d==28:
        return f"(1, '{months[m]}', {y})"
    
    else:
        return f"({d+1}, '{months[m-1]}', {y})"
    
