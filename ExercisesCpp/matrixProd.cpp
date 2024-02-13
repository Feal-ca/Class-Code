#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> Matrix;

void printMat(Matrix mat) {
  for (int i = 0; i < mat.size(); ++i) {
    for (int j = 0; j < mat.size(); ++j) {
      cout << mat[i][j] << " ";
    }
    cout << endl;
  }
}
Matrix product(const Matrix &a, const Matrix &b) {
  Matrix result(a.size(), vector<int>(a.size(), 0));
  for (int f = 0; f < a.size(); ++f) {
    for (int i = 0; i < a.size(); ++i) {
      for (int j = 0; j < a.size(); ++j) {
        result[f][j] += a[f][i] * b[i][j];
      }
    }
  }
  return result;
}

int main() {
  Matrix mat = {{1, 2, 3}, {2, 5, 8}, {3, 8, 9}};
  Matrix mat2 = {{1, 5, 2}, {1, 200, 9}, {4, 2, 5}};
  Matrix r(mat.size(), vector<int>(mat.size()));
  r = product(mat, mat2);

  printMat(r);
}
