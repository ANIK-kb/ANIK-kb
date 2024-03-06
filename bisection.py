def func(x):
   return x**2 - 4*x - 10

x1 = float(input("Enter first value:"))
x2 = float(input("Enter second value:"))
i=0

while func(x1)*func(x2)<0:
    x0 = (x1 + x2) / 2

    if func(x0) * func(x1) < 0:
        x2 = x0
    else:
        x1 = x0
    i=i+1
    if abs(x1-x2) <= 0.000000000001:
        break
root = (x1 + x2) / 2
print("The root is", root,"after",i,"iterations")
