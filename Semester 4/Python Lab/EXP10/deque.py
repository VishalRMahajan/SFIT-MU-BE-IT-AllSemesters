"""Implement queue using deque (deck) and show insertion of element from the rear side, deletion of element from the front side, rotate and extend queue"""


import collections
List = list()
de = collections.deque(List)
def Enqueue(de):
    a = int(input("Enter the element to add into queue: "))
    de.append(a)

def Dequeue(de):
    de.popleft()

def rotate(de):
    de.rotate(-1)

def Extend(de):
    n = int(input("Enter total number to extend: "))
    List1 = []
    print("Enter the elements:")
    for a in range(n):
        a = int(input())
        List1.append(a)
    de.extend(List1)

def Print(de):
    print("\n",de)

while(True):
    i=int(input("\nMenu of Deque\n1.Enqueue\n2.Dequeue\n3.Rotate\n4.Extend\n5.Print\n6.Exit\nEnter your choice: "))
    if i == 1:
        Enqueue(de)
    elif i == 2:
        Dequeue(de)
    elif i == 3:
        rotate(de)
    elif i == 4:
        Extend(de)
    elif i == 5:
        Print(de)
    elif i == 6:
        break

