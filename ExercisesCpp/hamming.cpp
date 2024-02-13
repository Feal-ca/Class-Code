#include <iostream>
#include <vector>
using namespace std;

bool is_hamming(int n) {
  if (n == 1) {
    return true;
  }
  if (n % 2 == 0) {
    return is_hamming(n / 2);
  } else if (n % 3 == 0) {
    return is_hamming(n / 3);
  } else if (n % 5 == 0) {
    return is_hamming(n / 5);
  } else {
    return false;
  }
}

int main() {
  int n;
  vector<int> nums;
  bool found = false;
  while (not found and cin >> n) {
    if (is_hamming(n)) {
      cout << n << endl;
      found = true;
    }
  }
  if (not found) {
    cout << 0 << endl;
  }
}
