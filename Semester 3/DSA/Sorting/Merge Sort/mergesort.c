#include <stdio.h>
#define len 9


void merge(int arr[], int beg, int mid, int end) {

  for (int i = beg; i <= end; i++) {
    printf("%d ", arr[i]);
  }

  int a = beg, b = mid + 1;
  int temp_arr[end - beg + 1];

 
  for (int i = 0; i < end - beg + 1; i++) {
    if (a > mid && b > end) {
      break;
    }
    else if (b > end) {
      temp_arr[i] = arr[a];
      a++;
    }
    else if (a > mid) {
      temp_arr[i] = arr[b];
      b++;
    }
    else if (arr[a] > arr[b]) {
      temp_arr[i] = arr[b];
      b++;
    }
    else {
      temp_arr[i] = arr[a];
      a++;
    }
  }


  printf("\nAfter sort: ");
  for (int i = 0; i < end - beg + 1; i++) {
    printf("%d ", temp_arr[i]);
    arr[beg + i] = temp_arr[i];
  }
  printf("\n\n");
}


void mergesort(int arr[], int beg, int end) {
  if (beg < end) {
    int mid = (beg + end) / 2;
    mergesort(arr, beg, mid);
    mergesort(arr, mid + 1, end);
    merge(arr, beg, mid, end); 
  }
}


void main() {
  int A[len];

 
  for (int i = 0; i < len; i++)
  {     
        printf("Enter the %d element of array: ",i+1);
        scanf("%d",&A[i]);
  }
  printf("\n\n");
 
  printf("Unsorted Array: ");
  for (int i = 0; i < len; i++) {
    printf("%d ", A[i]);
  }
  printf("\n\n");

  mergesort(A, 0, (len - 1)); 

  printf("Final Sorted Array: ");
  for (int i = 0; i < len; i++) {
    printf("%d ", A[i]);
  }
}
