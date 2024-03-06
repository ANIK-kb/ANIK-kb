x1=float(input("enter the x1 value:"))
y1=x1**3
print(f"for x1={x1} y1 is {y1}  ")

def dfunc(a):
    return 3*a**2

x2= float(input("enter the value of x2:"))
h=float(input("enter the step size:"))
i=0
while x1<x2:
    y2 = y1 + h*(dfunc(x1))
    y1=y2
    x1=x1+h
    print(y2)
    
    i=i+1
