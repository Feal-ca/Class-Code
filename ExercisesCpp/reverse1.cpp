#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string s;
  vector<string> words;
  string word;
  int n;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    cin >> s;
    word = "";
    for (char c : s) {
      word = c + word;
    }
    words.push_back(word);
  }
  for (int j = n - 1; j >= 0; --j) {
    cout << words[j] << endl;
  }
}
