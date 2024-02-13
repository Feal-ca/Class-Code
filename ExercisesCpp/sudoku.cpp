#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> Matrix;

void printMat(Matrix mat) {
  for (int i = 0; i < mat.size(); ++i) {
    for (int j = 0; j < mat[0].size(); ++j) {
      cout << mat[i][j] << " ";
    }
    cout << endl;
  }
}
bool solvedSudoku(const Matrix mat) {
  int prod = 0;
  // check rows
  for (int i = 0; i < 9; ++i) {
    for (int elem : mat[i]) {
      prod += pow(2, elem - 1);
    }
    // cout << prod << endl;
    if (prod != 511) {
      return false;
    }

    prod = 0;
  }
  // check columns
  for (int i = 0; i < 9; ++i) {
    for (int j = 0; j < 9; ++j) {
      int elem = mat[j][i];
      prod += pow(2, elem - 1);
    }
    // cout << prod << endl;
    if (prod != 511) {
      return false;
    }

    prod = 0;
  }
  // check columns
  for (int b = 0; b < 3; ++b) {
    for (int a = 0; a < 3; ++a) {

      for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
          int elem = mat[i + 3 * a][j + 3 * b];
          prod += pow(2, elem - 1);
        }
      }
      // cout << prod << endl;
      if (prod != 511) {
        return false;
      }

      prod = 0;
    }
  }
  return true;
}

int main() {
  Matrix mat(9, vector<int>(9));
  bool r;
  int n, element;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    for (int a = 0; a < 9; ++a) {
      for (int b = 0; b < 9; ++b) {
        cin >> element;
        mat[a][b] = element;
      }
    }
    r = solvedSudoku(mat);
    if (r) {
      cout << "yes" << endl;
    } else {
      cout << "no" << endl;
    }
  }
  // printMat(mat);
}
