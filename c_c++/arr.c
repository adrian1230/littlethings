#include <stdio.h>

/*
Given a 2D array arr[][] with each row of the form {l, r}, 
the task is to find a pair (i, j) such that 
the ith interval lies within the jth interval. 
If multiple solutions exist, then print anyone of them. 
Otherwise, print -1.
*/

int main()
{
  printf("enter the length of the integer list: ");
  int n;
  scanf("%d",&n);
  int data[n];
  for (int i = 0; i < n; ++i)
  {
    printf("n's val must smaller than (n + 1)'s val where n is an order number");
    int arr[2];
    printf("the first value: ");
    int val_1;
    scanf("%d",&val_1);
    printf("the second value: ");
    int val_2;
    scanf("%d",&val_2);
    arr[0] = val_1;
    arr[1] = val_2;
    // data[i] = arr;
  }
  return 0;
}
