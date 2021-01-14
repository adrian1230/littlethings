#include <stdio.h>

int main()
{
  printf("enter the length of the integer list: ");
  int n;
  scanf("%d",&n);
  int data[n];
  for (int i = 0; i < n; ++i)
  {
    int val;
    printf("give me an int: ");
    scanf("%d",&val);
    data[i] = val;
  }
  printf("%d \n",(int) (sizeof(data)/sizeof(data[0])));
  printf("%d \n",data[n-1]);
  return 0;
}
