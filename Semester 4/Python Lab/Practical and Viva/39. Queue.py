class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.append(element)
        print("After Enqueue, Queue is",self.queue)
    
    def dequeue(self):
        if len(self.queue) != 0:
            element = self.queue.pop(0)
            print("After Dequeue, Queue is",self.queue)
            return element
        else:
            print("Queue is Empty")

    def rotate(self):
        if len(self.queue) != 0:
            element = self.queue.pop(0)
            self.queue.append(element)
            print("After Rotate, Queue is",self.queue)
        else:
            print("Queue is Empty")

    def extend(self,Listofelements):
        self.queue.extend(Listofelements)
        print("After Extend, Queue is",self.queue)
    
    def printqueue(self):
        print("Queue is",self.queue)

queue = Queue()

while(True):
    print("\nMenu:\n1.Enqueue\n2.Dequeue\n3.Rotate\n4.Extend\n5.Print\n6.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter the element to add into queue: ")
        queue.enqueue(element)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.rotate()
    elif choice == 4:
        limit = int(input("Enter total number to extend: "))
        items = []
        print("Enter the elements: ")
        for i in range(limit):
            i = input()
            items.append(i)
        queue.extend(items)
    elif choice == 5:
        queue.printqueue()
    elif choice == 6:
        break
    else:
        print("Invalid choice")