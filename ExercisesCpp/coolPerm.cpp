#include <bits/fs_fwd.h>
#include <iostream>
#include <vector>
using namespace std;

void all_cool_permutations(int n, int i, vector<int> list, vector<bool> used,
                           int a, int b) {
  if (i == n) {
    for (int j = 0; j < n - 1; ++j) {
      cout << list[j] << " ";
    }
    cout << list[n - 1] << endl;
  } else {
    for (int x = 0; x < n; ++x) {
      if (not used[x] and x != a and x != b) {
        used[x] = true;
        list[i] = x;
        all_cool_permutations(n, i + 1, list, used, x + 1, x - 1);
        used[x] = false;
      }
    }
  }
}

void show_cool_permutations(int n) {
  vector<int> v(n, -1);
  vector<bool> u(n, false);
  all_cool_permutations(n, 0, v, u, -1, -1);
  cout << "********************" << endl;
}

int main() {
  int n;
  while (cin >> n) {
    show_cool_permutations(n);
  }
}
