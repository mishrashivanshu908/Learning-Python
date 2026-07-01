def CountEven():
  with open("numbers.txt","r") as f:
    data=f.read()
    numbers=data.split(",")
    print(type(numbers))#list of strings
    print(type(numbers[0]))#string
    count=0
    for i in numbers:
        if int(i)%2==0:
            count+=1
  return count  
    
print("The number of even numbers in the file are:", CountEven())