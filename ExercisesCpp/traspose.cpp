#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> Matrix;

void transpose(Matrix &m) {
  for (int i = 0; i < m.size(); ++i) {
    for (int j = i; j < m[0].size(); ++j) {
      swap(m[i][j], m[j][i]);
    }
  }
}
int main() {
  Matrix mat = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  transpose(mat);
  for (int a = 0; a < mat.size(); ++a) {
    for (int b = 0; b < mat.size(); ++b) {
      cout << mat[a][b] << " ";
    }
    cout << endl;
  }
}
