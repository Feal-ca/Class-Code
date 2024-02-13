#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

long long sum(vector<long long> list) {
  long long sum = 0;
  for (long long n : list) {
    sum += n;
  }
  return sum;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(2);

  long long n;
  while (cin >> n) {
    vector<long long> L(n);
    for (int i = 0; i < n; ++i) {
      cin >> L[i];
    }
    sort(L.begin(), L.end());
    int a = (n / 2) - 1;
    int b = (n / 2);
    long long s = sum(L);

    float result = max(abs(((s - L[a]) / float(n - 1)) - L[b]),
                       abs(((s - L[b]) / float(n - 1)) - L[a]));

    cout << s - L[a] << ", " << float(n - 1) << ", " << s << endl;
    cout << (s - L[a]) / float(n - 1) << ":" << L[b] << endl;

    cout << result << endl;
  }
}
