#include <stdio.h>

int main()
{
  printf("enter the length of the integer list: ");
  int n;
  scanf("%d",&n);
  int data[n];
  for (int i = 0; i < n; i++)
  {
    int val;
    printf("enter an int: ");
    scanf("%d",&val);
    data[i] = val;
  }
  for (int v = 0; v < (int) (sizeof(data)/sizeof(data[0])); ++v)
  {
    printf("%d \n",data[v]);
  }
  return 0;
}
