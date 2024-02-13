import math

def day_of_the_week(d,m,y):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    m = m-2
    if m <= 0:
        m=m+12
        y = y-1 
    c = y//100
    a = y%100
    #print(d,m,y,c,a)
    
    f = int((2.6*m)-0.2)+d+a+int(a/4)+int(c/4)-(2*c)    
    return days[int(f%7)]
if __name__ == "__main__":
    print(day_of_the_week(25, 10, 2023))
