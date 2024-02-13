#include <iostream>
#include <vector>
using namespace std;

void sieve(vector<bool> &primes) {
  for (int i = 2; (i * i) <= 1000002; ++i) {
    if (primes[i]) {
      for (int j = i * i; j <= 1000002; j += i) {
        primes[j] = false;
      }
    }
  }
}

int main() {
  int n;
  vector<bool> primes(1000002, true);
  primes[0] = false;
  primes[1] = false;

  sieve(primes);

  while (cin >> n) {
    if (primes[n]) {
      cout << n << " is prime" << endl;

    } else {
      cout << n << " is not prime" << endl;
    }
  }
}
