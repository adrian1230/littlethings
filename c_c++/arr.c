#include <stdio.h>

int main()
{
  printf("enter the length of the integer list: ");
  int n;
  scanf("%d",&n);
  int data[n];
  while ((int) (sizeof(data)/sizeof(data[0])) != n)
  {
    int len = (int) (sizeof(data)/sizeof(data[0])); 
    int val;
    printf("give me an int: ");
    scanf("%d",&val);
    data[len] = val;
  }
  printf("%d \n",(int) (sizeof(data)/sizeof(data[0])));
  printf("%d \n",data[-1]);
  return 0;
}
