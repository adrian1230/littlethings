// 0 <= num <= 2^31 - 1

#include <iostream>

using namespace std;

int main()
{
  int n;
  cout << "give a positive integer <= 10: " << endl;
  cin >> n;
  if (n < 1)
  {
    throw 20;
  }
  if (n > 10) {
    throw 20;
  }
  if (n==1){
    cout << "One" << endl;
  } else if (n == 2) {
    cout << "two" << endl;
  }
  else {
    cout << "omg" << endl;
  }
  return 0;
}
