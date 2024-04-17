#include <stdio.h>

//Stdlib is used for malloc Function
#include <stdlib.h>

/*Creating a LinkedList with data as integer and a address Node Next that 
will have address of next Node*/
struct Node
{
    int data;
    struct Node* Next;
};

//Creating a Pointer Top to contain the address of first Node of LinkedList or Stack
struct Node* Top=NULL;

/*we create a NewNode with refrence to Node and assign it memory using malloc function*/
void Push()
{   
   struct Node* NewNode;

   /* (struct Node*) is used for typecasting
   malloc is function in stdlib
   sizeof is used ti get size of struct node and assign it to NewNode */
   NewNode= (struct Node*)malloc(sizeof(struct Node));

   printf("Enter The Value to be Pushed: ");
   int PushValue;
   scanf("%d",&PushValue);

   /*value is pushed to created node's data and 
   we change the Next value to Top as in stack a element is push at a top means we are inserting at Begining
   and NewNode address to top. This means when we add a new node again top will get newnode address and 
   newnode next will get the address of previous node*/
   NewNode->data=PushValue;
   NewNode->Next=Top;
   Top=NewNode;
}


/*Check if Stack is empty or not and then create a new node and give it address of first node as
Stack is LIFO this means Top Most Node will be Poped. make top point to second node and using free predefined function
free the memory allocated to the poped node*/
void Pop()
{   
   if(Top==NULL)
   {
      printf("Stack Empty");
   }
   else
   {
      struct Node* Traversal=Top;
      printf("Node Pooped Out is %d \n",Traversal->data);
      Top=Top->Next;
      free(Traversal);
   }

}

//Check if stack is empty or not if not empty print data of top most node using top , arrow operator and data
void Peek()
{  if(Top==NULL)
      printf("Stack Empty");
   
   else
      printf("TopMost Element in Stack is %d",Top->data);
}


/* Use the concept of Traversal in linked list, Create a temp Pointer Traversal and assign it Top value 
then check if Stack is empty or not and in last just change the next to others node address using arrow
operator */
void display()
{    
   struct Node* Traversal=Top;

   if(Traversal==NULL)
   {
      printf("Stack is Empty");
   }
   while (Traversal !=NULL)
   {
      printf("%d ",Traversal->data);
      Traversal=Traversal->Next;
   }
   
    
}

int main()
{
    //Declearing integer choice for switch case and loop for while loop
    int choice,Loop=1;

    //while loop is used to make the switch case run again and again till loop integer is change other than 1
    while(Loop==1)
    {
         printf("+----Menu---+\n");
         printf("| 1.Push    |\n");
         printf("| 2.Pop     |\n");
         printf("| 3.Peek    |\n");
         printf("| 4.Display |\n");
         printf("+-----------+\n");
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