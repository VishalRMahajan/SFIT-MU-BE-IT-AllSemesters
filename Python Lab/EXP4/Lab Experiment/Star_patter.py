#Print Pattern (star pattern) using for or while loop

#Using for Loop
print("Using for Loop")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

#Using while Loop
print("Using while Loop")
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print("\n")
    i+=1