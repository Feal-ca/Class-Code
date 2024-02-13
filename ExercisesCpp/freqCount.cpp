#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  int count = 0;
  vector<int> nums;
  cin >> n;
  int num;

  for (int i = 0; i < n; ++i) {
    cin >> num;
    nums.push_back(num);
  }
  sort(nums.begin(), nums.end());

  if (nums.size() != 0) {

    int last = nums[0];
    for (int a : nums) {
      if (a == last) {
        count += 1;
      } else {
        cout << last << " : " << count << endl;
        count = 1;
        last = a;
      }
    }
    cout << last << " : " << count << endl;
  }
}
