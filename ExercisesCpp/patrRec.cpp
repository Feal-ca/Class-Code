#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<bool>> Matrix;
void show_mat(Matrix m) {
  for (vector<bool> L : m) {
    for (bool b : L) {
      if (b) {
        cout << "# ";
      } else {
        cout << ". ";
      }
    }
    cout << endl;
  }
}

void fill_pattern(int x, int y, int n, Matrix &mat) {
  if (n == 1) {
    mat[x][y] = true;
  } else {
    int d = pow(2, n - 1);

    fill_pattern(x, y, n - 1, mat);
    mat[x + d - 1][y] = true;

    fill_pattern(x + d, y, n - 1, mat);
    mat[x][y + d - 1] = true;

    fill_pattern(x, y + d, n - 1, mat);
    mat[x + (pow(2, n) - 2) - d + 1][y + pow(2, n) - 2] = true;

    fill_pattern(x + d, y + d, n - 1, mat);
    mat[x + (pow(2, n) - 2)][y + (pow(2, n) - 2) - d + 1] = true;
  }
}

int main() {
  int n;
  cin >> n;
  Matrix mat(pow(2, n) - 1, vector<bool>(pow(2, n) - 1, false));
  fill_pattern(0, 0, n, mat);
  show_mat(mat);
}
