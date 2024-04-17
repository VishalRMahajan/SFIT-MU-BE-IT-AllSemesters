#include <stdio.h>
#include <stdlib.h>

struct node
{
   int data;
   struct node *next;
};

struct queue
{
   struct node *front, *rear;
};

struct queue *createQueue()
{
   struct queue *q = (struct queue *)malloc(sizeof(struct queue));
   q->front = q->rear = NULL;
   return q;
}

void Enqueue(struct queue *q, int data)
{
   struct node *newNode = (struct node *)malloc(sizeof(struct node));
   newNode->data = data;
   newNode->next = NULL;

   if (q->rear == NULL)
   {
      q->front = q->rear = newNode;
      return;
   }

   q->rear->next = newNode;
   q->rear = newNode;
}

void Dequeue(struct queue *q)
{
   if (q->front == NULL)
   {
      printf("Queue is empty.\n");
      return;
   }

   struct node *temp = q->front;
   q->front = q->front->next;

   if (q->front == NULL)
   {
      q->rear = NULL;
   }

   free(temp);
}

void Display(struct queue *q)
{
   if (q->front == NULL)
   {
      printf("Queue is empty.\n");
      return;
   }

   struct node *temp = q->front;
   while (temp != NULL)
   {
      printf("%d ", temp->data);
      temp = temp->next;
   }
   printf("\n");
}

int main()
{
   // Create an empty queue
   struct queue *q = createQueue();

   // Declearing integer choice for switch case and loop for while loop
   int choice, Loop = 1, data;

   // while loop is used to make the switch case run again and again till loop integer is change other than 1
   while (Loop == 1)
   {
      printf(" ----Menu--- \n");
      printf("| 1.Enqueue   |\n");
      printf("| 2.Dequeue   |\n");
      printf("| 3.Display   |\n");
      printf("| 4.Exit      |\n");
      printf(" ----------- \n");
      printf("Enter the Choice: ");
      scanf("%d", &choice);

      switch (choice)
      {
      case 1:
         printf("Enter the data to Enqueue: ");
         scanf("%d", &data);
         Enqueue(q, data);
         break;

      case 2:
         Dequeue(q);
         break;

      case 3:
         Display(q);
         break;

      case 4:
         // we use return 0  to exit the menu
         return 0;
         break;

      default:
         printf("Please! Enter Valid Choice");
      }

      printf("Do you want to Continue(Enter 1 to Continue or Any other Number to Exit: ");
      scanf("%d", &Loop);
   }

   return 0;
}
