#include <iostream>
#include <vector>
using namespace std;

vector<double> merge(const vector<double> &v1, const vector<double> &v2) {
  vector<double> result;
  int i = 0;
  int j = 0;
  while (i < v1.size() and j < v2.size()) {

    if (v2[j] < v1[i]) {
      result.push_back(v2[j]);
      ++j;
    } else {
      result.push_back(v1[i]);
      ++i;
    }
  }
  while (i < v1.size()) {
    result.push_back(v1[i]);
    ++i;
  }
  while (j < v2.size()) {
    result.push_back(v2[j]);
    ++j;
  }
  return result;
}

int main() {
  vector<double> a{2, 3, 4, 4, 4, 4, 4, 4, 9};
  vector<double> b{1, 1, 3, 4, 4, 10, 11, 13};
  vector<double> c = merge(a, b);
  for (double d : c) {
    cout << d << " ";
  }
}
