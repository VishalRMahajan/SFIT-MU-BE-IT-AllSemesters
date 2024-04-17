#include <stdio.h>

//defining Max Limit of Queue
#define max 5

//Declaring Queue as Array
int queue[max];

//Declaring front and rear 
int front=-1;
int rear=-1;

void Enqueue()
{   
    //if rear is last index of array it will show output as Queue Overflow
    if(rear==max-1)
        printf("Queue Overflow \n");

    /* Here First Front and Rear will be checked for null value 
        if null value is found we change front and rear to 0 to 
        access 0th element of array if not we simply increment rear 
        to access next index of array
        at last we take element from user and use rear position to enqueue
        element in array */
    else
    {
        if(front==-1&rear==-1)
        {
            front=0;
            rear=0;
        }
        else
        {
            rear++;
        }
            int x;
            printf("Enter the element to be Inserted: \n");
            scanf("%d",&x);
            queue[rear]=x;
    }
}

void Dequeue()
{   
    /* we check if front is null or if it exceed index value of last element 
    as rear is used to access last element of queue  */
    if(front==-1||front >rear)
    {
        printf("Queue Underflow \n");
    }
    /* if first case if false we check if the element that we are dequeue 
     is the first element of the queue if it is first element of the queue
     we simply change front and rear value to null/-1 */
    else if(front==rear)
    {   
        printf("Dequeued Element is %d",queue[front]);
        front=rear=-1;    
    }
    /* if both the case is false we simply increment front 
        as front is use to access the first element of the queue*/
    else
    {
        printf("Dequeued Element is %d",queue[front]);
        front++;
    }

}

void Display()
{   
    /* we check if front is null or if it exceed index value of last element 
    as rear is used to access last element of queue  */
    if(front==-1||front>rear)
    {
        printf("Queue Empty \n");
    }
    /* we use for loop from front to rear to print queue */
    else
    {
        for (int i = front; i <= rear; i++)
        {
            printf("%d ",queue[i]);
        }
         printf("\n");
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
         printf("| 1.Enqueue   |\n");
         printf("| 2.Dequeue   |\n");
         printf("| 3.Display   |\n");
         printf("| 4.Exit      |\n");
         printf(" ----------- \n");
         printf("Enter the Choice: ");
         scanf("%d",&choice);
    
   
        switch(choice)
        {
             case 1:
               Enqueue();
             break;

             case 2:
                Dequeue();
             break;

             case 3:
                Display();
             break;

             case 4:
             //we use return 0  to exit the menu
                return 0;
             break;

             default:
                printf("Please! Enter Valid Choice");

            
        }

        printf("Do you want to Continue(Enter 1 to Continue or Any other Number to Exit: ");
        scanf("%d",&Loop);
        
    }

            return 0;
}