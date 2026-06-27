def calcFact(n):
  if n==1 or n==0:
    return 1
  return n*calcFact(n-1)
n=int(input("enter number to get its factorial: "))
print("factorial of",n,"is",calcFact(n))