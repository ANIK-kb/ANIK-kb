
def mparx(x): #partial derivative respect to x
   return -2*x
def mpary(y): #partial derivative respect to y
   return -4*y 

x1= float(input("enter the value of x1:"))
y1= float(input("enter the value of y1:"))
lamda= float(input("enter the step size:"))
i=0
while True:
   x2= x1 + lamda*mparx(x1)
   y2= y1 + lamda*mpary(y1)
   
   if abs(x2-x1) <=0.000001 or abs(y2-y1) <= 0.000001:
      break
   else:
      x1=x2
      print(f"value of x at {i} iteration:{x2}")
      y1=y2
      print(f"value of y at {i} iteraion:{y2}")
   i=i+1

print(f"the root of x is {x2} taken {i} iteration \n the root of y is {y2} taken {i} iteration")

