#include <stdio.h>


//Defining Max Element of Stack
#define max 5 

//Declearing Stack
int Stack[max];

//Declearing Top as Null or -1 (So that when incremented it will get value 0 i.e. array stack first element)
int top=-1;

void Push()
{   
    //Checking If Stack is Full 
    if(top==max-1)
        printf("Stack Overflow");
    
    //Taking Element From user ,incrementing the index of array and assigning taken value to the index i.e. Top
    else
    {
        int x;
        printf("Enter The Number to Be Pushed: ");
        scanf("%d",&x);
        top++;
        Stack[top]=x;
    }
}

void Pop()
{   
    //Checking if Stack is Empty 
    if(top==-1)
        printf("Stack UnderFlow");

    /*
     As Top point to last element of array and Stack is LIFO, 
     we show last element in Array using Stack,
     and reduce the Top 
    */
    else
    {
        printf("Number Poped is %d \n",Stack[top]);
        top--;
    }
}

void Peek()
{
    printf("TopMost Element in Stack is %d \n",Stack[top]);
}

void display()
{   
    //using for loop to display the Stack, incrementing i till top as top is the position of the topmost element in stack
    for (int i = 0; i <= top; i++)
    {
        printf("%d  ",Stack[i]);
    }
    
}

int main()
{
    //Declearing integer choice for switch case and loop for while loop
    int choice,Loop=1;

    //while loop is used to make the switch case run again and again till loop integer is change other than 1
    while(Loop==1)
    {
         printf(" ----Menu--- \n");
         printf("| 1.Push    |\n");
         printf("| 2.Pop     |\n");
         printf("| 3.Peek    |\n");
         printf("| 4.Display |\n");
         printf(" ----------- \n");
         printf("Enter the Choice: ");
         scanf("%d",&choice);
    
   
        switch(choice)
        {
             case 1:
               Push();
             break;

             case 2:
                Pop();
             break;

             case 3:
              Peek();
             break;

             case 4:
                display();
             break;

             default:
                printf("Please! Enter Valid Choice");

            
        }

        printf("Do you want to Continue(Enter 1 to Continue or Any other Number to Exit: ");
        scanf("%d",&Loop);
        
    }

            return 0;
}