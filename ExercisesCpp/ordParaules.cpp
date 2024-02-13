#include <execution>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool compare(string a, string b) {
  if (isupper(a[0]) and not isupper(b[0]))
    return false;
  else if (isupper(b[0]) and not isupper(a[0]))
    return true;
  else if (a.size() > b.size())
    return false;
  else if (b.size() > a.size())
    return true;
  else if (a > b)
    return false;
  else if (a < b)
    return true;
}

void merge(vector<string> &v, int l, int m, int r) {
  vector<string> b(r - l + 1);
  int i = l;
  int j = m + 1;
  int k = 0;
  while (i <= m and j <= r) {
    if (compare(v[i], v[j])) // True if v[i]<v[j]
      b[k++] = v[i++];
    else
      b[k++] = v[j++];
  }
  while (i <= m)
    b[k++] = v[i++];
  while (j <= r)
    b[k++] = v[j++];
  for (k = 0; k <= r - l; ++k)
    v[l + k] = b[k];
}

void merge_sort_1(vector<string> &v, int l, int r) {
  if (l < r) {
    const int m = (l + r) / 2;
    merge_sort_1(v, l, m);
    merge_sort_1(v, m + 1, r);
    merge(v, l, m, r);
  }
}

void merge_sort_1(vector<string> &v) { merge_sort_1(v, 0, v.size() - 1); }

void ordenar(vector<string> &paraules) { merge_sort_1(paraules); }

int main() {
  string s;
  vector<string> p;
  while (cin >> s) {
    p.push_back(s);
  }
  ordenar(p);

  for (string s : p) {
    cout << s << endl;
  }
}
