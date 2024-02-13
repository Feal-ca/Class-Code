#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  int count = 0, max_count = 0;
  while (n != 0) {
    cin >> n;
    vector<string> lst(n);
    for (int i = 0; i < n; ++i) {
      cin >> lst[i];
    }
    sort(lst.begin(), lst.end());
    string last = lst[0];
    string word = lst[0];
    for (int i = 1; i < lst.size(); ++i) {
      if (last != lst[i]) {
        count = 0;
      }
      ++count;
      if (count >= max_count) {
        max_count = count;
        word = lst[i];
      }
    }
    cout << word << endl;
  }
}
