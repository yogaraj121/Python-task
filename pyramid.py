n=int(input("enter the limit:"))

for i in range(0,n+1):
    
  for j in range(i,n):
      print(" ",end=" ")
  for k in range(0,2*i-1):
      print("*",end=" ")
  print()
