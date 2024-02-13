#include <iostream>
#include <vector>
using namespace std;

void selsort(vector<double> &V) {
  const int n = V.size();
  for (int i = 0; i < n - 1; ++i) {
    int least = i;
    for (int j = i + 1; j <= n - 1; ++j) {
      if (V[j] < V[least]) {
        least = j;
      }
    }
    swap(V[i], V[least]);
  }
}

int main() { // nothing
  /*vector<double> V{};

  selsort(V);
  for (double d : V) {
    cout << d << " ";
  }*/
  return 0;
}
