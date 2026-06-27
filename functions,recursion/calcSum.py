def calcSum(a=2,b=3):
  return a+b

for i in range(2):
  a=int(input("enter first number: "))
  b=int(input("enter second number: "))
  print("sum of",a,"and",b,"is",calcSum(a,b))
print("sum->",calcSum())