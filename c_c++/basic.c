#include <stdio.h>
#include <stdlib.h>

int main(){
  char hero_name[] = "Jo";
  int hero_age = 19;
  printf("this is %s and she is %d\n",hero_name,hero_age);
  char grade[10];
  printf("enter the final grade: ");
  fgets(grade,10,stdin);
  printf("grade: %s \n",grade);
  double exp;
  printf("yr work exp: ");
  scanf("%lf",&exp);
  printf("year of work experience %f \n",exp);
  return 0;
}
