numb=int(input("enter number of subjects: "))
dict={}
for i in range(0,numb):
  subject=input("enter subject: ")
  marks=float(input("enter marks of above subject: "))
  dict[subject]=marks
  #can also use => dict.update({subject,marks})

print(dict)