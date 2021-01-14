#include <stdio.h>

int main()
{
  printf("enter the length of the integer list: ");
  int n;
  scanf("%d",&n);
  int data[] = {};
  while ((int) (sizeof(data)/sizeof(data[0])) != n ) {
    int len = (int) sizeof(data) / sizeof(data[0]);
    int val;
    printf("enter a value as of integer: ");
    scanf("%d",&val);
    data[len] = val;
  }
  return 0;
}
