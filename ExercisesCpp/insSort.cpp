#include <iostream>
#include <vector>
using namespace std;

void insertion_sort(vector<double> &v) {
  const int n = v.size();

  for (int i = 1; i < n; ++i) {
    for (int j = i; j > 0 && v[j - 1] > v[j]; --j) {
      swap(v[j - 1], v[j]);
    }
  }
}

int main() {
  vector<double> a{5, 4, 3, 2, 1, 0};
  insertion_sort(a);
  for (double d : a) {
    cout << d << " ";
  }
}
