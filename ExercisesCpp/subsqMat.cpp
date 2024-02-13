#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> Board;

void show_matrix(Board &b) {
  for (vector<int> L : b) {
    for (int n : L) {
      cout << n << " ";
    }
    cout << endl;
  }
  cout << endl;
}

bool is_valid_subsq(Board &b, int i, int j) {
  vector<bool> nums(9, false);
  int c = 0;
  for (int i2 = 0; i2 < 3; ++i2) {
    for (int j2 = 0; j2 < 3; ++j2) {
      if (nums[b[i + i2][j + j2]]) {
        return false;
      } else {
        nums[b[i + i2][j + j2]] = true;
      }
    }
  }
  return true;
}

int find_subsquares(Board &b) {
  int count = 0;
  for (int i = 0; i < b.size() - 2; ++i) {
    for (int j = 0; j < b[0].size() - 2; ++j) {
      if (is_valid_subsq(b, i, j)) {
        ++count;
      }
    }
  }
  return count;
}

int main() {
  int n, m, x;
  while (cin >> n >> m) {
    Board b(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> x;
        b[i][j] = x;
      }
    }

    int n_sub_squares = find_subsquares(b);
    cout << n_sub_squares << endl;
  }
}
