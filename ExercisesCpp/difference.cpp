#include <iostream>
#include <vector>
using namespace std;

vector<double> difference(const vector<double> &v1, const vector<double> &v2) {
  vector<double> result;
  int i = 0;
  int j = 0;
  while (i < v1.size() and j < v2.size()) {

    if (v1[i] == v2[j]) {
      ++i;
    } else if (v1[i] > v2[j]) {
      ++j;
    } else {
      if (result.empty() or result.back() != v1[i]) {
        result.push_back(v1[i]);
      }
      ++i;
    }
  }
  while (i < v1.size()) {
    if (result.empty() or result.back() != v1[i]) {
      result.push_back(v1[i]);
    }
    ++i;
  }
  return result;
}

int main() {
  vector<double> a{1, 2, 2, 3, 4, 5, 5, 7};
  vector<double> b{0, 0, 2, 3, 3, 5, 9};
  vector<double> c = difference(a, b);
  for (double d : c) {
    cout << d << " ";
  }
}
