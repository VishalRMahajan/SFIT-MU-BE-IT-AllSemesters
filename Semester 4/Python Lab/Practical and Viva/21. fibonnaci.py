a=0
b=1

for i in range(10):
    print(a)
    temp=a
    a=b
    b=b+temp

n=10
a=0
b=1
while(n!=0):
    print(a)
    temp=a
    a=b
    b=b+temp
    n=n-1