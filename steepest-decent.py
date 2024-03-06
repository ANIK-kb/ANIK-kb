def func(x):
   return x**2 - 4*x - 10
def der(x):
   return 4- 2*x
x1= float(input("enter the guess point:"))
lamda= float(input("enter the step size:"))
i=1
while True:
   x2=x1 + lamda*der(x1)
   
   
   if abs(x2-x1) <= 0.000001:
      break
   else:
      x1=x2
      
   i=i+1
print(f"the root is {x2} and iteration taken {i} ")