#include <iostream>
#include <vector>
using namespace std;

void show(vector<char> list) {
  for (char c : list) {
    cout << c;
  }
  cout << endl;
}

void paraules_supercreixents_rec(int n, int i, vector<char> L) {
  if (n == i) {
    show(L);
  } else {
    for (int x = L[0]; x <= 'z'; ++x) {
      if (x - L[i - 1] >= 2) {
        L[i] = x;
        paraules_supercreixents_rec(n, i + 1, L);
      }
    }
  }
}

void paraules_supercreixents(int n, char p) {
  vector<char> L(n, ' ');
  L[0] = p;

  paraules_supercreixents_rec(n, 1, L);
}

int main() {
  int n;
  char p;
  cin >> n;
  cin >> p;

  paraules_supercreixents(n, p);
}
