import math
def func1():
    th,x=eval(input())
    y=x*math.tan(math.pi*th/180)
    y=round(y,2)
    print("%.2f"%y)
func1()