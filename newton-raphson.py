def func(x):
   return x**2 - 4*x - 10
def der(x):
   return 2*x-4  

x1 = float(input("Enter a guess:"))
i=1
while True:
   x2= (x1-(func(x1)/der(x1)))
   
   x1=x2

   if abs(func(x1)) <=0.0000001:
      break
   i=i+1
print(f"the root is {x1} and it takes {i} iterations")