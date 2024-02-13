#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

typedef vector<vector<bool>> Board;

void read_virus_pos(Board &b, vector<tuple<int, int>> &v, int &c) {
  char ch;
  for (int i = 0; i < b.size(); ++i) {
    for (int j = 0; j < b[0].size(); ++j) {
      cin >> ch;
      if (ch == 'X') {
        b[i][j] = true;
        v.push_back(tuple<int, int>(i, j));
        ++c;
      }
    }
  }
}

void show_matrix(Board b) {
  for (vector<bool> L : b) {
    for (bool t : L) {
      if (t) {
        cout << "X";
      } else {
        cout << ".";
      }
    }
    cout << endl;
  }
}

void next_step(Board &b, vector<tuple<int, int>> &v, int &c) {
  vector<tuple<int, int>> v2;
  for (tuple<int, int> t : v) {
    int i = get<0>(t);
    int j = get<1>(t);


    if (i > 0) {
      if (not b[i - 1][j]) {
        b[i - 1][j] = true;
        ++c;
        v2.push_back(tuple<int, int>(i - 1, j));
      }
    }
    if (i < b.size() - 1) {
      if (not b[i + 1][j]) {
        b[i + 1][j] = true;
        ++c;
        v2.push_back(tuple<int, int>(i + 1, j));
      }
    }
    if (j > 0) {
      if (not b[i][j - 1]) {
        b[i][j - 1] = true;
        ++c;
        v2.push_back(tuple<int, int>(i, j - 1));
      }
    }
    if (j < b[0].size() - 1) {
      if (not b[i][j + 1]) {
        b[i][j + 1] = true;
        ++c;
        v2.push_back(tuple<int, int>(i, j + 1));
      }
    }
  }
  v = v2;
}

int main() {
  int n, m, c;
  while (cin >> n) {
    cin >> m;
    c = 0;
    Board b(n, vector<bool>(m, false));
    vector<tuple<int, int>> v;

    read_virus_pos(b, v, c);
    show_matrix(b);
    cout << endl;

    while (c < n * m) {
      next_step(b, v, c);
      show_matrix(b);
      cout << endl;
    }
    cout << "----------" << endl;
  }
}
