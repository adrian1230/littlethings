#include <iostream>
#include <vector>
#include <array>
#include <iterator>

using namespace std;

int main()
{
  int n;
  cout << "enter the length of the Big array: " << endl;
  cin >> n;
  std::vector<int> data;
  int c = 0;
  while (c != n)
  {
    int arr[2]={};
    int val_1;
    printf("1st val: ");
    scanf("%d",&val_1);
    int val_2;
    printf("2nd val: ");
    scanf("%d",&val_2);
    arr[0] = val_1;
    arr[1] = val_2;
    data.insert(data.end(),std::begin(arr),std::end(arr));
    c += 1;
  }
  return 0;
}
