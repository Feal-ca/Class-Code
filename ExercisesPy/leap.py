def is_leap_year(year):
    if year%100==0:
        if (year//100)%4==0:
            return True
    elif year%4==0:
        return True
    return False

