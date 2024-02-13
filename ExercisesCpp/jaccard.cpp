#include <iostream>
#include <vector>
using namespace std;

float intersection(vector<int> v1, vector<int> v2) {
  int i = 0;
  int j = 0;
  vector<int> intersec;
  float inter = 0.0;
  while (i < v1.size() and j < v2.size()) {
    if (v1[i] == v2[j]) {
      ++inter;
      intersec.push_back(v1[i]);
      ++j;
      ++i;
    } else if (v1[i] < v2[j]) {
      ++i;
    } else {
      ++j;
    }
  }
  return inter;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(3);

  int n1, n2;
  int x;
  while (cin >> n1) {
    vector<int> v1(n1);
    for (int i = 0; i < n1; ++i) {
      cin >> x;
      v1[i] = x;
    }
    cin >> n2;
    vector<int> v2(n2);
    for (int i = 0; i < n2; ++i) {
      cin >> x;
      v2[i] = x;
    }

    float inters = intersection(v1, v2);
    float result = (inters) / ((n1 + n2) - inters);
    cout << result << endl;
  }
}
