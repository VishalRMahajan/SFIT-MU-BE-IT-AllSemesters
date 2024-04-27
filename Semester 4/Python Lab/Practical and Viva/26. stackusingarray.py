import array

class Stack:
    def __init__(self):
        self.stack = array.array("i")

    def push(self,element):
        self.stack.append(element)
        print("After Pushing element,",element,"in the stack,stack is",self.stack)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("After Poping element,",self.stack.pop(),"from the stack,stack is",self.stack)
        pass

    def top(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top Element of the Stack is",self.stack[-1])
        pass

stack = Stack()

while(True):

    choice = int(input("\n1.Push\n2.Pop\n3.Top\n4.Exit\nEnter Your Choice:"))

    if choice == 1:
        element = int(input("Enter the Element to be Pushed: "))
        stack.push(element)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.top()
    elif choice == 4:
        break
    else:
        print("Enter Right Choice")