"""Write a Python program to implement a stack using an array."""

import array

# Initialize an empty array as a stack
stack = array.array('i')

# Push operation
def push(val):
    stack.append(val)

# Pop operation
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        return stack.pop()

# Display stack
def display():
    print(stack)


while(True):
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter the value to push: "))
        push(val)
    elif choice == 2:
        popped = pop()
        if popped is not None:
            print(f"Popped element: {popped}")
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")