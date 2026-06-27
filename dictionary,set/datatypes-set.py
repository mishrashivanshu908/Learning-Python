set={9,9.0,9.25,'9.0'}
set2={("float",9.0),("int",9)}
for i in set:
  print(i,type(i))
print("--------")
for i in set2:
  print(i[1],type(i[1]))