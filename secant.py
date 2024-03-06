def func(x):
   return x**2 - 4*x - 10

x1 = float(input("Enter first value:"))
x2 = float(input("Enter second value:"))
i=1
while True:
   x3= (x2 - ((func(x2)*(x2-x1))/(func(x2)-func(x1))))
   x1=x2
   x2=x3
   print(x1)
   print(x2)
   
   if abs(x2-x1) <= 0.0000001:
      break
   i=i+1

print("the root is:",x3,"\n""iteration taken:",i)