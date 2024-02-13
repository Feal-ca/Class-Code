#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> Matrix;

Matrix sum(const Matrix &a, const Matrix &b) {
  Matrix result(a.size(), vector<int>(a.size()));
  for (int i = 0; i < a.size(); ++i) {
    for (int j = 0; j < a.size(); ++j) {
      result[i][j] = a[i][j] + b[i][j];
    }
  }
  return result;
}
int main() {
  Matrix mat = {{1, 2, 3}, {2, 5, 8}, {3, 8, 9}};
  Matrix mat2 = {{1, 2, 3}, {2, 5, 8}, {3, 8, 9}};
  Matrix r(mat.size(), vector<int>(mat.size()));
  r = sum(mat, mat2);
  for (int i = 0; i < mat.size(); ++i) {
    for (int j = 0; j < mat.size(); ++j) {
      cout << r[i][j] << " ";
    }
    cout << endl;
  }
}
