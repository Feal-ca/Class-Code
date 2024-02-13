#include <iostream>
#include <vector>
using namespace std;

int position_maximum(const vector<double> &v, int m) {
  int posMax = 0;
  for (int i = 0; i <= m; ++i) {
    if (v[i] > v[posMax]) {
      posMax = i;
    }
  }
  return posMax;
}
int main() { // Not used
  const vector<double> v{0, 1, 12, 3, 4, 5, 6, 80};
  cout << position_maximum(v, 7) << endl;
  return 0;
}
