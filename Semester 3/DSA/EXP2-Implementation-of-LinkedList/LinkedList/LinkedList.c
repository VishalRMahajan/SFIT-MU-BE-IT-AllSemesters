/*Write a C program to implement the Singly linked list using switch case that includes
operations like
       i. creation (42-65)
      ii.  Insert
          a. In the beginning
          b. After a node
          c. At the end

     iii.  Delete
          a. In the beginning
          b. Given node
          c. At the end

     iv.  Count
      v.  Search
     vi.  reverse
    vii.  Display

Code Simplified: Creation of newnode:   struct node *newnode;//node pointer
                                        newnode = (struct node *)malloc(sizeof(struct node)); //allocate memory using malloc and typecast it
                                        newnode->data = datatobeinserted;  //This will be used to add value in data of newnode
                                        newnode->next = NULL; //This will be used to connect it to new node

                  Traversal to the end: tempfortraversal = head; // point a temp pointer to head
                                        while (tempfortraversal->next != NULL) //use loop to traverse to the node who have next value as null(last node)
                                        {
                                             tempfortraversal = tempfortraversal->next;//we will use next block so that we can traverse to next node
                                        }
                                        

Traversal to last and last second node: tempfortraversal = head;
                                        struct node *prev_node = NULL;
                                        while (tempfortraversal->next != NULL)
                                        {
                                            prev_node = tempfortraversal;
                                            tempfortraversal = tempfortraversal->next;
                                         }
                                        
*/

#include <stdio.h>
#include <stdlib.h>



/*create a singly linked list and two pointer one as a head(top) and Other as a temporary pointer for traversal*/
struct node
{
    int data;
    struct node *next;
} *head, *tempfortraversal;





/*Take data from user to be inserted, create a newnode, check for case
 1 case is that created node may be first node that means we need to add its address to head and
 2nd case is default case, we simply traverse to the end and update the next of last node to created node */
void CreationofLinkedList(int datatobeinserted)
{
    struct node *newnode;
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = datatobeinserted;
    newnode->next = NULL;

    if (head == NULL)
    {
        head = newnode;
    }
    else
    {
        tempfortraversal = head;
        while (tempfortraversal->next != NULL)
        {
            tempfortraversal = tempfortraversal->next;
        }
        tempfortraversal->next = newnode;
    }
}



/*create a new node and change it next to head this will make created node to point to earlier first node 
and then make head point to newnode this will make newnode as first node i.e. insertion at beg*/
void insertionatbeg(int datatobeinserted)
{
    struct node *newnode;
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = datatobeinserted;
    newnode->next = head;

    head = newnode;
}


/*create a new node , use traversal to traverse the linklist , use if statement for condition in which the node is found
if node is found update the newnode next with the node next and node's next with newnode,*/
void insertionafteranode(int datatobeinserted, int afternode)
{
    struct node *newnode;
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = datatobeinserted;
    newnode->next = NULL;

    tempfortraversal = head;

    while (tempfortraversal != NULL)
    {
        if (tempfortraversal->data == afternode)
        {
            newnode->next = tempfortraversal->next;
            tempfortraversal->next = newnode;
            return;
        }
        tempfortraversal = tempfortraversal->next;
    }
    printf("Node %d not found", afternode);
}

/*create a new node , check for condition 1st conditon is if linked list is empty update head with newnode
and if not default condition traverse to the end and when reached end change next of last node to point to the
newnode*/
void insertionatend(int datatobeinserted)
{
    struct node *newnode;
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = datatobeinserted;
    newnode->next = NULL;

    if (head == NULL)
    {
        head = newnode;
    }
    else
    {
        tempfortraversal = head;
        while (tempfortraversal->next != NULL)
        {
            tempfortraversal = tempfortraversal->next;
        }
        tempfortraversal->next = newnode;
    }
}

/*Check if linkedlist is empty if not default condition i.e. use a temp pointer, set temp pointer to head i.e. make it point to
node to be deleted,move the head to next node using temp->next and free the first node*/
void deletitioninbeg()
{
    if (head == NULL)
        printf("Linked List Empty \n");

    else
    {
        tempfortraversal = head;
        printf("Node Deleted is %d \n", tempfortraversal->data);
        head = tempfortraversal->next;
        free(tempfortraversal);
    }
}


/*decleare a prev pointer ; check condition 1st check if node is empty ; if not use loop to traverse to the given node
condition of loop should be node should not be null and node;s data should not be equal to given data so that when desired node is found
we can exit the loop; then check if tempfortraversal is null this means givennode is not there in our linkedlist; 
In last 2 condition for deletion,  1st is if node that we want to delete is first node simply update head to point to next node and if not i.e. default condition
we will use prev pointer that is pointing to previous node and make it to the next node of node we are going to delete using tempfortraversal->next; in last free the 
node */
void deletitiongivennode(int givennode)
{
    struct node *prev_node = NULL;
    if (head == NULL)
        printf("Linked List Empty \n");

    else
    {
        tempfortraversal = head;

        while (tempfortraversal != NULL && tempfortraversal->data != givennode)
        {
            prev_node = tempfortraversal;
            tempfortraversal = tempfortraversal->next;
        }

        if (tempfortraversal == NULL)
        {
            printf("Node with Data %d not found", givennode);
        }

        if (prev_node == NULL)
        {
            head = tempfortraversal->next;
        }
        else
        {
            prev_node->next = tempfortraversal->next;
        }

        printf("Node Deleted is %d \n", tempfortraversal->data);
        free(tempfortraversal);
    }
}

/*decleare a prev pointer ; check condition 1st check if node is empty ; if not use loop to traverse to last and second last node;
after reaching last free the last node,Now we set the next of second last pointer to null as after deletion it will become last node
use if conditon to check for condition , 1st is if prev_node is not null set its next to null and if it null means deleted node was first node
so set head to null ,*/
void deletitonatend()
{
    struct node *prev_node = NULL;

    if (head == NULL)
        printf("Linked List Emmpty \n");

    else
    {
        tempfortraversal = head;

        while (tempfortraversal->next != NULL)
        {
            prev_node = tempfortraversal;
            tempfortraversal = tempfortraversal->next;
        }
        printf("Node Deleted is %d \n", tempfortraversal->data);
        free(tempfortraversal);

        if (prev_node != NULL)
        {
            prev_node->next = NULL;
        }
        else
        {
            head = NULL;
        }
    }
}

/*Use a variable and traverse the linkedlist while incrementing the variable ,In last print the variable*/
void count()
{
    int count = 0;
    tempfortraversal = head;

    while (tempfortraversal != NULL)
    {
        count++;
        tempfortraversal = tempfortraversal->next;
    }
    printf("Total No. of elements in Linked List is %d \n", count);
}

/*use two variable position one for position and other to use as boolean; we simply traverse to end and if found we print the position if not
 we printf not found*/
void search(int element)
{
    int position = 0, found = 0;
    tempfortraversal = head;

    while (tempfortraversal != NULL)
    {
        if (tempfortraversal->data == element)
        {
            printf("Element %d found at position %d \n", element, position);
            found = 1;
        }
        position++;
        tempfortraversal = tempfortraversal->next;
    }

    if (found != 1)
    {
        printf("%d element is not in Linked List \n", element);
    }
}


/*we use three pointer prev current and next and we traverse through list and set the current node adddress to point to prev node and then 
prevnode to current and current to nextnode and then using nextnode->next we traverse to furthur node and in last as head is still pointing to 
earlier first node we change it to point to current first i.e. earlier last*/
void reverse()
{
    struct node *prevnode, *currentnode, *nextnode;
    prevnode = NULL;
    currentnode = nextnode = head;

    while (nextnode != NULL)
    {
        nextnode = nextnode->next;
        currentnode->next = prevnode;
        prevnode = currentnode;
        currentnode = nextnode;
    }
    head = prevnode;
}

/*Simply travesal to end while printing the current node also check if linked list is empty*/
void Display()
{
    struct node *Displaytraversal;
    Displaytraversal = head;

    if (Displaytraversal == NULL)
    {
        printf("LinkedList is Empty \n");
    }
    else
    {
        while (Displaytraversal != NULL)
        {
            printf("%d ", Displaytraversal->data);
            Displaytraversal = Displaytraversal->next;
        }
        printf("\n");
    }
}

int main()
{
    // Declearing integer choice for switch case and loop for while loop
    int choice, Loop = 1, val, n, after, given;
    ;

    // while loop is used to make the switch case run again and again till loop integer is change other than 1
    while (Loop == 1)
    {
        printf("+-------------Menu---------------+ \n");
        printf("| 1. Creating a Linked List      |\n");
        printf("| 2. Insertion in the Beginning  |\n");
        printf("| 3. Insertion After a Node      |\n");
        printf("| 4. Insertion At the end        |\n");
        printf("| 5. Deletion in the beginning   |\n");
        printf("| 6. Deletion of a Given Node    |\n");
        printf("| 7. Deletion At the end         |\n");
        printf("| 8. Count No. of Elements       |\n");
        printf("| 9. Search Element              |\n");
        printf("| 10.Reverse the LinkedList      |\n");
        printf("| 11.Display                     |\n");
        printf("| 12.Exit                        |\n");
        printf("+--------------------------------+\n");
        printf("Enter the Choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:

            printf("Enter the Number of Nodes to be Created: ");
            scanf("%d", &n);

            while (n != 0)
            {
                printf("Enter the Data to be inserted: ");
                scanf("%d", &val);
                CreationofLinkedList(val);
                n--;
            }

            break;

        case 2:
            printf("Enter the Data to be inserted: ");
            scanf("%d", &val);
            insertionatbeg(val);
            break;

        case 3:

            printf("Enter the node after which to be inserted: ");
            scanf("%d", &after);

            printf("Enter the Data to be inserted: ");
            scanf("%d", &val);
            insertionafteranode(val, after);

            break;

        case 4:
            printf("Enter the Data to be inserted: ");
            scanf("%d", &val);
            insertionatend(val);
            break;

        case 5:
            deletitioninbeg();
            break;

        case 6:
            printf("Enter the node to be deleted: ");
            scanf("%d", &given);
            deletitiongivennode(given);
            break;

        case 7:
            deletitonatend();
            break;

        case 8:
            count();
            break;

        case 9:
            printf("Enter the element/data to be searched: ");
            scanf("%d", &val);
            search(val);
            break;

        case 10:
            reverse();
            break;

        case 11:
            Display();
            break;

        case 12:
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