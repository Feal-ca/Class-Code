#include <iostream>
#include <vector>
using namespace std;

int position(double x, const vector<double> &v, int left, int right) {
  if (left <= right) {
    int m = (left + right) / 2;

    if (v[m] == x) {
      return m;
    } else if (v[m] < x) {
      return position(x, v, m + 1, right);
    } else {
      return position(x, v, left, m - 1);
    }
  }
  return -1;
}
int main() { // Not used
  const vector<double> v{0, 1, 2, 3, 4, 5, 6, 8};
  cout << position(8, v, 0, v.size() - 1) << endl;
  return 0;
}
