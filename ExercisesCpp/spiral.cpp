#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<char>> Matrix;

struct Position {
  // Member variables
  int x;
  int y;

  Position(int initialX, int initialY) : x(initialX), y(initialY) {}

  void update(int newX, int newY) {
    x = newX;
    y = newY;
  }
};

void printMat(Matrix mat) {
  for (int i = 0; i < mat.size(); ++i) {
    for (int j = 0; j < mat[0].size(); ++j) {
      cout << mat[i][j] << " ";
    }
    cout << endl;
  }
  if (mat.size() > 0)
    cout << endl;
}
void draw_line(Matrix &mat, int x1, int y1, int x2, int y2) {
  if (x1 == x2) {
    int b = max(y1, y2);
    for (int a = min(y1, y2); a <= b; ++a) {
      mat[x1][a] = 'X';
    }
  } else {
    int b = max(x1, x2);
    for (int a = min(x1, x2); a <= b; ++a) {
      mat[a][y1] = 'X';
    }
  }
}
void make_spiral(Matrix &mat, int n) {
  int c = 0;
  Position pos(n - 1, 0);
  for (int i = n - 1; i >= 0; --i) {
    if (c % 4 == 0) {
      draw_line(mat, pos.x, pos.y, pos.x, pos.y + i);
      pos.update(pos.x - 1, pos.y + i);
    } else if (c % 4 == 1) {
      draw_line(mat, pos.x, pos.y, pos.x - i, pos.y);
      pos.update(pos.x - i, pos.y - 1);
    } else if (c % 4 == 2) {
      draw_line(mat, pos.x, pos.y, pos.x, pos.y - i);
      pos.update(pos.x + 1, pos.y - i);
    } else if (c % 4 == 3) {
      draw_line(mat, pos.x, pos.y, pos.x + i, pos.y);
      pos.update(pos.x + i, pos.y + 1);
    }
    ++c;
  }
}
int main() {
  int n;

  while (cin >> n) {
    Matrix spiral(n, vector<char>(n, '.'));

    make_spiral(spiral, n);
    printMat(spiral);
  }
}
