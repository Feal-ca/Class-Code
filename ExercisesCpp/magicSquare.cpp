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
bool zigZag(Matrix mat) {
  int element = mat[0][0];
  int last = mat[0][0] - 1;

  for (int i = 0; i < mat[0].size(); ++i) {
    if (i % 2 == 0) {
      for (int j = 0; j < mat.size(); ++j) {
        element = mat[j][i];
        if (last >= element) {
          return false;
        }
        last = element;
      }
    } else {
      for (int j = mat.size() - 1; j >= 0; --j) {
        element = mat[j][i];
        if (last >= element) {
          return false;
        }

        last = element;
      }
    }
  }
  return true;
}

int main() {
  int n, m, element;
  int c = 1;
  while (cin >> m) {
    cin >> n;

    Matrix mat(m, vector<int>(n));
    for (int a = 0; a < m; ++a) {
      for (int b = 0; b < n; ++b) {
        cin >> element;
        mat[a][b] = element;
      }
    }
    bool r = zigZag(mat);
    cout << "matriu " << c << ": ";
    ++c;
    if (r) {
      cout << "yes" << endl;
    } else {
      cout << "no" << endl;
    }
  }
  // printMat(mat);
}
