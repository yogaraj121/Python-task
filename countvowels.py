word=input("enter the word:")
vowels={'a','e','i','o','u'}
d={}
for i in word:
    d[i]=d.get(i,0)+1
for k in shorted(d.items(i)):
    print(k ,"times")
