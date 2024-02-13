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
Matrix product(const Matrix &a, const Matrix &b) {
  Matrix result(a.size(), vector<int>(b[0].size(), 0));
  for (int f = 0; f < a.size(); ++f) {
    for (int i = 0; i < b.size(); ++i) {
      for (int j = 0; j < b[0].size(); ++j) {
        result[f][j] += a[f][i] * b[i][j];
      }
    }
  }
  return result;
}

int main() {
  Matrix mat = {{1, 2, 3}, {4, 5, 6}};
  Matrix mat2 = {{1, 2, 3, 4}, {58, 5, 5, 5}, {5, 5, 5, 5}};
  Matrix r(mat.size(), vector<int>(mat.size()));
  r = product(mat, mat2);

  printMat(r);
}
