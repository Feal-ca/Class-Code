#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int repeticiones(const vector<string> &lst, int i) {
  int n = lst.size();
  int r = 1, j = i + 1;
  while (j < n and lst[j] == lst[i]) {
    ++r;
    ++j;
  }

  return r;
}

int main() {
  int n;
  while (cin >> n) {
    vector<string> lst(n);
    for (int i = 0; i < n; ++i) {
      cin >> lst[i];
    }
    sort(lst.begin(), lst.end());

    vector<int> cont(n + 1, 0);
    int i = 0;

    while (i < n) {
      int r = repeticiones(lst, i);
      cont[r] += lst[i].size();
      i = i + r;
    }

    for (int i = 0; i <= n; ++i) {
      if (cont[i] != 0) {
        cout << i << " : " << cont[i] << endl;
      }
    }
  }
}
