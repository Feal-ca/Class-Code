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

bool isZigZag(Matrix m) {
  int elem;
  for (int a = 0; a < m.size(); ++a) {
    for (int b = 0; b < m[0].size(); ++b) {
      m[a][b] = elem;
    }
  }
}

int main() {
  int n, m, elem;
  cin >> n;
  cin >> m;
  Matrix mat(n, vector<int>(m));
  for (int a = 0; a < n; ++a) {
    for (int b = 0; b < m; ++b) {
      cin >> elem;
      mat[a][b] = elem;
    }
  }
  if (isZigZag(mat)) {
    cout << "yes" << endl;
  } else {
    cout << "no" << endl;
  }
}
