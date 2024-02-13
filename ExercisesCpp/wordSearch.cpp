#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef vector<vector<char>> Board;
typedef vector<vector<int>> Points;

int place_word(int i, int j, string w, const Board &b, const Points &p,
               int max_points) {
  bool placeable = true;
  if (i + w.size() <= b.size()) {
    int points = 0;
    for (int z = 0; z < w.size(); ++z) {
      if (w[z] != b[i + z][j]) {
        placeable = false;
        break;
      } else {
        points += p[i + z][j];
      }
    }
    if (placeable and points > max_points) {
      max_points = points;
    }
  }

  placeable = true;
  if (j + w.size() <= b[0].size()) {
    int points = 0;
    for (int z = 0; z < w.size(); ++z) {
      if (w[z] != b[i][j + z]) {
        placeable = false;
        break;
      } else {
        points += p[i][j + z];
      }
    }
    if (placeable and points > max_points) {
      max_points = points;
    }
  }
  return max_points;
}
int get_points(string s, Board &b, Points &p) {
  int points = -1;
  for (int i = 0; i < b.size(); ++i) {
    for (int j = 0; j < b[0].size(); ++j) {
      points = place_word(i, j, s, b, p, points);
    }
  }
  return points;
}

int main() {
  int n, m;
  char c;
  int x;
  while (cin >> n >> m) {
    Board b(n, vector<char>(m));
    Points p(n, vector<int>(m));

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> c;
        b[i][j] = c;
      }
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        cin >> x;
        p[i][j] = x;
      }
    }
    int n_w;
    string s;
    cin >> n_w;
    vector<string> ws(n_w);
    for (int i = 0; i < n_w; ++i) {
      cin >> s;
      int total_points = get_points(s, b, p);
      if (total_points == -1) {
        cout << "no" << endl;
      } else {
        cout << total_points << endl;
      }
      ws[i] = s;
    }
  }
}
