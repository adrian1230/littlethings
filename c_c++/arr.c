#include <stdio.h>

int main()
{
  printf("enter the length of the integer list: ");
  int n;
  scanf("%d",&n);
  int data[n];
  for (int i = 0; i < n; ++i)
  {
    int arr[2];
    for (int t = 0; t < 2; ++t)
    {
    }
    int val;
    printf("give me an int: ");
    scanf("%d",&val);
    data[i] = val;
  }
  return 0;
}
