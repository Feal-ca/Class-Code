#include <iostream>
#include <vector>
using namespace std;

bool es_suma(vector<int> numbers) {
  /* Donada una llista de nombres, diu si algun nombre de la llista és o no la
   * suma de la resta. */
  int sum = 0;
  for (int i = 0; i < numbers.size(); ++i) {
    sum = sum + numbers[i];
  }
  for (int i = 0; i < numbers.size(); ++i) {
    if (sum - numbers[i] == numbers[i]) {
      return true;
    }
  }

  return false;
}

int main() {
  int n, x;
  vector<int> numbers;
  while (cin >> n) {
    numbers.clear();
    for (int i = 0; i < n; ++i) {
      cin >> x;
      numbers.push_back(x);
    }
    if (es_suma(numbers)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
