#include <iostream>
#include <vector>
using namespace std;

vector<double> merge2(vector<double> v1, vector<double> v2) {
  if (v1.size() == 0) {
    return v2;
  }
  if (v2.size() == 0) {
    return v1;
  }

  double x = v1.back();
  double y = v2.back();

  if (x >= y) {
    v1.pop_back();
    vector<double> r = merge2(v2, v1);
    r.push_back(x);
    return r;
  } else {
    v2.pop_back();
    vector<double> r = merge2(v2, v1);
    r.push_back(y);
    return r;
  }
}
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

vector<double> mergesort2(vector<double> v, int l, int r) {
  int size = v.size();
  if (size <= 1) {
    return v;
  }
  vector<double> left;
  vector<double> right;
  for (int i = 0; i < (size / 2); ++i) {
    left.push_back(v[i]);
  }
  for (int i = (size / 2); i < (size); ++i) {
    right.push_back(v[i]);
  }
  return merge2(mergesort2(left), mergesort2(right));
}
void mergesort(vector<double> &V) { V = mergesort2(V); }

int main() {
  vector<double> a{1, 4, 5, 0, 1, 3, 7, 6, 8, 9, 3, 44, 5};
  mergesort(a);
  for (double d : a) {
    cout << d << " ";
  }
}
