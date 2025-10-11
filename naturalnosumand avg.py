## to display the first 10 natural numbers
n=int(input("enter your natural number:"))
sum=0
for i in range(1,11):
    print(i)
    sum+=i
print(sum)
avg=sum/10
print(avg)
