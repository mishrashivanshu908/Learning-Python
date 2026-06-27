n=int(input("enter number till which you want factorial: "))
fact=1
for i in range(1,n+1):
  fact*=i
  print("factorial of",i,":",fact)