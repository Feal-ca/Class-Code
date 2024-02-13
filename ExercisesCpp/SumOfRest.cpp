#include <iostream>
#include <vector>
using namespace std;

bool itemEqualToSum(double sum, vector<double> list) {
  for (int i = 0; i < list.size(); ++i) {
    if (sum - list[i] == list[i]) {
      return true;
    }
  }
  return false;
}

int main() {
  int n;
  double element, sum;
  vector<double> nums;
  while (cin >> n) {
    sum = 0;
    nums.clear();

    for (int i = 0; i < n; ++i) {
      cin >> element;
      sum = sum + element;
      nums.push_back(element);
    }

    if (itemEqualToSum(sum, nums)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
