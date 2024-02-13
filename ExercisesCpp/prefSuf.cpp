#include <iostream>
#include <vector>
using namespace std;

int pref_suf(int n, const vector<int>& list) {
  int sum = 0;
  int c = n - 1;
  int target = list[n - 1];
  for (int i = 0; i < n; ++i) {

    sum += list[i];
    while (sum > target) {
      --c;
      target += list[c];
    }
    // cout << target << " : " << sum << endl;
    if (sum == target) {
      return i + 1;
    }
  }
  return -1;
}

int main() {
  int n;
  while (cin >> n) {
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
      cin >> nums[i];
    }
    cout << pref_suf(n, nums) << endl;
  }
}
