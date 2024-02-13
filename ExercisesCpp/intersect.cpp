#include <iostream>
#include <vector>
using namespace std;

vector<double> intersection(const vector<double> &v1,
                            const vector<double> &v2) {
  vector<double> result;
  int i = 0;
  int j = 0;
  while (i < v1.size() and j < v2.size()) {

    if (v1[i] < v2[j]) {
      ++i;
    } else if (v1[i] > v2[j]) {
      ++j;
    } else {
      if (result.empty() or result.back() != v1[i]) {
        result.push_back(v1[i]);
      }
      ++i;
      ++j;
    }
  }

  return result;
}

int main() {
  vector<double> a{0, 0, 1, 1.2, 1.2};
  vector<double> b{0, 1, 1.2};
  vector<double> c = intersection(a, b);
  for (double d : c) {
    cout << d << " ";
  }
}
