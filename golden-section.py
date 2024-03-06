def func(x):
   return x**2 - 4*x - 10

a=float(input("enter first guess point:"))
b=float(input("enter second guess point:"))
i=1
while True:
   x1= (b - (0.618*(b-a)))
   x2= (a + (0.618*(b-a)))

   if func(x1)<func(x2):
      b=x2
   else:
      a=x1
   if abs(func(x1)-func(x2)) <= 0.000001:
      break
   i=i+1
print(f"the root is {x1} and iteration taken {i}") 