#include <stdio.h>


/* selection sort takes three variable for accessing index, same as bubble sort we use loop till n-1
then we set a min_index pointer to the element not sorted i.e. i and use other variable to compare it with 
other elements in array when we find element less than min_index element we assign index of that element to min_index using third
variable then we simply perform swapping and print it*/
void selectionsort(int ar[], int n)
{
    int i, j, min_index, temp;

    for (i = 0; i < n - 1; i++)
    {
        min_index = i ;
        for (j = i+1; j < n; j++)
        {
            if (ar[j] < ar[min_index])
            {
                min_index = j;
            }
        }
        temp = ar[min_index];
        ar[min_index] = ar[i];
        ar[i] = temp;
    }

    
}

int main()
{
    int n;

    printf("Enter the size of array: ");
    scanf("%d", &n);

    int ar[n];
    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d element: ", i + 1);
        scanf("%d", &ar[i]);
    }

    printf("Original array is : \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", ar[i]);
    }

    selectionsort(ar, n);

    printf("\n");
    printf("sorted array is : \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", ar[i]);
    }

    return 0;
}