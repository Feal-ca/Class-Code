#include <iostream>
#include <vector>
using namespace std;

void show(vector<int> a) {
  for (int n : a) {
    cout << n << ", ";
  }
  cout << endl;
}

void perms_emparellades_rec(int n, int i, vector<int> L, vector<bool> used,
                            int &c) {
  if (i == n) {
    show(L);
    ++c;
  } else {
    for (int x = 0; x < n; ++x) {
      if (not used[x]) {
        if (i % 2 == 0) {
          if (i == 0) {
            L[i] = x;
            used[x] = true;
            perms_emparellades_rec(n, i + 1, L, used, c);
            used[x] = false;

          } else if (x % 2 == L[0] % 2) {
            L[i] = x;
            used[x] = true;
            perms_emparellades_rec(n, i + 1, L, used, c);
            used[x] = false;
          }

        } else if (i % 2 == 1) {
          if (i == 1) {
            L[i] = x;
            used[x] = true;
            perms_emparellades_rec(n, i + 1, L, used, c);
            used[x] = false;
          } else if (L[i - 2] < x) {
            L[i] = x;
            used[x] = true;
            perms_emparellades_rec(n, i + 1, L, used, c);
            used[x] = false;
          }
        }
      }
    }
  }
}

int perms_emparellades(int n) {
  int c = 0;
  perms_emparellades_rec(n, 0, vector<int>(n, 0), vector<bool>(n, false), c);
  return c;
}

int factorial(int n) {
  if (n == 0 or n == 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

int solution(int n) {
  if (n == 0) {
    return 0;
  }
  if (n % 2 == 1) {
    return factorial((n + 1) / 2);
  } else {
    return 2 * factorial(n / 2);
  }
}

int main() {
  int n;
  while (cin >> n) {
    int r = perms_emparellades(n);
    // int r = solution(n);
    cout << r << endl;
  }
}
