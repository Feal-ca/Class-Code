#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<int>> Matrix;

bool is_symmetric(Matrix &m) {
  for (int i = 0; i < m.size(); ++i) {
    for (int j = i; j < m[0].size(); ++j) {
      if (m[i][j] != m[j][i]) {
        return false;
      }
    }
  }
  return true;
}
int main() {
  Matrix mat = {{1, 2, 3}, {2, 5, 8}, {3, 8, 9}};
  cout << is_symmetric(mat) << endl;
}
