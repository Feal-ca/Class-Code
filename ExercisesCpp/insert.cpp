#include <iostream>
#include <vector>
using namespace std;

void insert(vector<double> &v) {
  const double value = v.back();
  const int n = v.size();

  int c = 0;
  while (v[c] < value) {
    ++c;
  }

  for (int i = c; i < n - 1; ++i) {
    swap(v[i], v[n - 1]);
  }
}

int main() {
  vector<double> a{1, 2, 3, 4, 5, 6, 7, 4};
  cout << a.back() << endl;
  insert(a);
  for (double d : a) {
    cout << d << " ";
  }
}
