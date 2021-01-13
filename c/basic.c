#include <stdio.h>
#include <stdlib.h>

int main(){
  char hero_name[] = "Jo";
  int hero_age = 19;
  printf("this is %s and she is %d\n",hero_name,hero_age);
  double yr_of_work_exp;
  char final_grade;
  printf("year of work exp: ");
  scanf("%lf",&yr_of_work_exp);
  printf("final grade: ");
  scanf("%c",&final_grade);
  printf("%f",yr_of_work_exp);
  printf("%c",final_grade);
  return 0;
}
