#include <iostream>
#include <vector>
using namespace std;

typedef vector<char> rowchar;
typedef vector<rowchar> matrixchar;
typedef vector<int> rowint;
typedef vector<rowint> matrixint;

matrixchar read(const int n, const int m) {
  matrixchar mat(n + 1, rowchar(m + 1, '.'));
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      char caracter;
      cin >> caracter;
      mat[i][j] = caracter;
    }
  }
  return mat;
}

int happysum(const matrixchar &mat, const int n, const int m) {
  matrixint ct1(n + 1, rowint(m + 1, 0)); // contador ':'
  matrixint ct2(n + 1, rowint(m + 1, 0)); // contador '-'
  matrixint ct3(n + 1, rowint(m + 1, 0)); // contador ')'
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      ct1[i][j] = ct1[i - 1][j] + ct1[i][j - 1] - ct1[i - 1][j - 1];
      ct2[i][j] = ct2[i - 1][j] + ct2[i][j - 1] - ct2[i - 1][j - 1];
      ct3[i][j] = ct3[i - 1][j] + ct3[i][j - 1] - ct3[i - 1][j - 1];
      if (mat[i][j] == ':')
        ++ct1[i][j];
      else if (mat[i][j] == '-')
        ct2[i][j] += ct1[i - 1][j - 1];
      else if (mat[i][j] == ')')
        ct3[i][j] += ct2[i - 1][j - 1];
    }
  }
  return ct3[n][m];
}

int main() {
  int n, m;
  while (cin >> n >> m) {
    matrixchar mat = read(n, m);
    cout << happysum(mat, n, m) << endl;
  }
}
