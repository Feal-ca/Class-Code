#include <iostream>
#include <vector>
using namespace std;

int pos_min(vector<double> &V, int l, int r) {
  int p = l;
  for (int j = l + 1; j <= r; ++j) {
    if (V[j] < V[p]) {
      p = j;
    }
  }
  return p;
}
void sel_sort(vector<double> &V) {
  const int n = V.size();
  for (int i = 0; i < n - 1; ++i) {
    const int p = pos_min(V, i, n - 1);
    swap(V[i], V[p]);
  }
}

int main() {
  vector<double> a{};
  sel_sort(a);
  for (double d : a) {
    cout << d << " ";
  }
}
