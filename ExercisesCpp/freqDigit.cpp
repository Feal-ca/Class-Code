#include <iostream>
#include <vector>
using namespace std;

int main() {
  int b, n;
  vector<int> digitCount(10, 0);

  cin >> b;

  while (cin >> n) {
    while (n >= b) {
      digitCount[n % b] += 1;
      n = n / b;
    }

    digitCount[n] += 1;
  }
  int max = 0;
  for (int a = 1; a < digitCount.size(); ++a) {
    if (digitCount[max] < digitCount[a]) {
      max = a;
    }
  }
  cout << max << " " << digitCount[max] << endl;
}
