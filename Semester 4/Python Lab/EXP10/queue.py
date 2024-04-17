"""
Create a user defined module to implement a data structure queue. The module should perform the following functions:
		1. Enqueue element from the rear side
		2. Dequeue element from the front side
		3. Rotate the queue
        4. Extend queue
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def rotate(self):
        if not self.is_empty():
            temp = self.dequeue()
            self.enqueue(temp)

    def extend(self, items):
        self.items.extend(items)

    def is_empty(self):
        return len(self.items) == 0
    
queue = Queue()

while(True):
    i = int(input("\nMenu of User Defined\n1.Enqueue\n2.Dequeue\n3.Rotate\n4.Extend\n5.Print\n6.Exit\nEnter your choice: "))
    if i == 1:
        item = input("Enter the element to add into queue: ")
        queue.enqueue(item)
    elif i == 2:
        queue.dequeue()
    elif i == 3:
        queue.rotate()
    elif i == 4:
        n = int(input("Enter total number to extend: "))
        items = []
        print("Enter the elements: ")
        for a in range(n):
            a = input()
            items.append(a)
        queue.extend(items)
    elif i == 5:
        print("\n", queue.items)
    elif i == 6:
        break
    else:
        print("Invalid choice")






