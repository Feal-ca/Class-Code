#include <iostream>
using namespace std;

bool is_palindrome(const string &s) {
  for (int i = 0; 2 * i <= s.size(); ++i) {
    if (s[i] != s[s.size() - 1 - i])
      return false;
  }
  return true;
}
