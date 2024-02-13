#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int rows, cols, element;
  string request;
  cin >> rows >> cols;

  vector<vector<int>> mtx(rows, vector<int>(cols));

  for (int i = 0; i < rows; ++i) {
    for (int j = 0; j < cols; ++j) {
      cin >> element;
      mtx[i][j] = element;
    }
  }
  int a, b;
  while (cin >> request) {
    if (request == "row") {
      cin >> a;
      cout << "row " << a << ":";
      for (int d : mtx[a - 1]) {
        cout << " " << d;
      }
      cout << endl;
    } else if (request == "element") {
      cin >> a >> b;
      cout << "element " << a << " " << b << ": ";
      cout << mtx[a - 1][b - 1] << endl;
    } else if (request == "column") {
      cin >> b;
      cout << "column " << b << ":";
      for (int i = 0; i < rows; ++i) {
        cout << " " << mtx[i][b - 1];
      }
      cout << endl;
    }
  }
}
