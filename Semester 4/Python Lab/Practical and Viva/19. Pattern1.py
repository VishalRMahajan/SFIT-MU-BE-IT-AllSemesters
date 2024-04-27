pattern = ("A","C","E","G","I")

for i in range(6):
    for j in range(i):
        print(pattern[j],end=" ")
    print("\n")