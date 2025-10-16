n=985
for i in range(4,0,-1):
    for j in range(0,4-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(n),end=" ")
    print()
