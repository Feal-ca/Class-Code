#include <iostream>
#include <vector>
using namespace std;

vector<int> sieve_eratostenes(int m) {
  vector<int> sieve(m + 1, 0);
  sieve[0] = 0;
  sieve[1] = 1;
  int i = 2;
  while (i <= m) {
    if (sieve[i] == 0) {
      sieve[i] = i;
      for (int j = 2 * i; j <= m + 1; j += i) {
        sieve[j] = i;
      }
    }
    i += 1;
  }
  /*for (int i = 0; i <= m + 1; ++i) {
    if (sieve[i] == 0) {
      sieve[i] = i;
    }
  }*/
  return sieve;
}
int main() {
  int n;
  vector<int> finished_sieve = sieve_eratostenes(1000000);
  while (cin >> n) {
    int c = 1;
    int i = n;
    vector<vector<int>> divisors;
    while (i != 1) {
      int d = finished_sieve[i];
      bool used = false;
      for (int i = 0; i < divisors.size(); ++i) {
        if (divisors[i][0] == d) {
          divisors[i][1] = divisors[i][1] + 1;
          used = true;
        }
      }
      if (not used) {
        divisors.push_back({d, 1});
      }
      i = i / d;
    }
    for (vector<int> a : divisors) {
      c *= a[1] + 1;
    }
    cout << c << endl;
  }
}
