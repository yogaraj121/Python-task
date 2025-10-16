a=" i am new to this office but not new to role"
b=a.split()
print(b)
for i in set(b):
    print(i,"-occurance to:",b.count(i))
