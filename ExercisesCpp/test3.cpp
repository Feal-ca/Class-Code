#include <iostream>
#include <vector>
using namespace std;

int fun(vector<int> a, int n) {
  if (n == 1)
    return a[0];
  int x = fun(a, n - 1);
  if (x > a[n - 1])
    return x;
  return a[n - 1];
}
int main() {
  vector<int> v = {12, 10, 30, 50, 100};
  cout << fun(v, 5) << endl;
}
