#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool is_digit(char c) {
  char result = false;
  for (char a : "0123456789") {
    if (c == a) {
      result = true;
    }
  }
  return result;
}
string suma(int b, string x, string y) {
  vector<char> digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8',
                         '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
  int max_length = max(x.size(), y.size());
  x = string(max_length - x.size(), '0') + x;
  y = string(max_length - y.size(), '0') + y;

  string result = "";
  int carry = 0;
  int A, B;

  for (int i = max_length - 1; i >= 0; --i) {
    if (is_digit(x[i])) {
      A = int(x[i]) - 48;
    } else {
      A = int(x[i] - 55);
    }
    if (is_digit(y[i])) {
      B = int(y[i]) - 48;
    } else {
      B = int(y[i] - 55);
    }
    int s = A + B + carry;
    carry = s / b;
    result = digits[s % b] + result;
  }
  if (carry == 0) {
    return result;
  } else {

    return digits[carry] + result;
  }
}

int main() {
  int b;
  string x, y;
  while (cin >> b >> x >> y) {
    cout << suma(b, x, y) << endl;
  }
}
