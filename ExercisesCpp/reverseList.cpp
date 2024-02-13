#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> nums;
  int n, element;
  while (cin >> n) {
    for (int i = 0; i < n; ++i) {
      cin >> element;
      nums.push_back(element);
    }

    for (int a = nums.size() - 1; a >= 1; --a) {
      cout << nums[a] << " ";
    }

    if (not nums.empty()) {
      cout << nums[0] << endl;
    } else {
      cout << endl;
    }
    nums.clear();
  }
}
