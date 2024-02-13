#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool contains(string word, char letter) {
  for (char c : word) {
    if (c == letter) {
      return true;
    }
  }
  return false;
}

bool is_tuti(string word, string hex) {
  for (char c : hex) {
    if (not contains(word, c)) {
      return false;
    }
  }
  return true;
}

bool is_valid_word(string w, string hex, char lt) {
  if (w.size() <= 2) {
    return false;
  }
  if (not contains(w, lt)) {
    return false;
  }
  for (char c : w) {
    if (not contains(hex, c)) {
      return false;
    }
  }
  return true;
}
int main() {
  int punts = 0;
  vector<string> words;
  vector<string> goodWords;
  string letters, word;
  cin >> letters;
  char lt = letters[0];

  while (cin >> word) {
    words.push_back(word);
  }

  for (string w : words) {

    if (is_valid_word(w, letters, lt)) {
      goodWords.push_back(w);

      if (w.size() == 3) {
        punts += 1;
      } else if (w.size() == 4) {
        punts += 2;
      } else {
        punts += w.size();
      }

      if (is_tuti(w, letters)) {
        punts += 10;
      }
    }
  }
  sort(goodWords.begin(), goodWords.end());
  for (string w : goodWords) {
    cout << w << endl;
  }
  cout << "-----" << endl;
  cout << punts << endl;
}
