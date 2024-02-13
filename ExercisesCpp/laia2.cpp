#include <iostream>
#include <vector>
using namespace std;

int prefix_sufix(vector<int> v, int n) {
  int j = n - 2;
  int i = 1;
  int prefix = v[0];
  int sufix = v[n - 1];
  while (true) {
    cout << prefix << " : " << sufix << endl;
    if (prefix == sufix)
      return i;
    else if (prefix < sufix) {
      prefix += v[i];
      i++;
    } else {
      sufix += v[j];
      --j;
    }
  }
  return -1;
}

int main() {
  int n;
  cin >> n;
  vector<int> v(n);
  for (int i = 0; i < n; ++i) {
    cin >> v[i];
  }
  int prefix = prefix_sufix(v, n);
  cout << prefix << endl;
}
