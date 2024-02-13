#include <iostream>
#include <string>
#include <vector>
using namespace std;

string patro_recursiu(char s) {
  if (s == 'a') {
    return ("a");
  } else {
    string last = patro_recursiu(s - 1);
    string result = "";
    for (int i = 0; i < s - 97; ++i) {
      result = result + last + s;
    }
    result = s + result;
    return result;
  }
}
int main() {
  char s;
  cin >> s;
  cout << patro_recursiu(s) << endl;
}
