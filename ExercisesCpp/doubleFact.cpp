#include <iostream>
using namespace std;

int double_factorial(int x) {
  if (x == 0 or x == 1) {
    return 1;
  }
  for (int i = x - 2; i > 0; i -= 2) {
    x *= i;
  }
  return x;
}

int main() {
  int n;
  cin >> n;
  cout << double_factorial(n) << endl;
}
