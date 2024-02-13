#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct Word {
  string word;
  int freq;
};
static bool customCompare(const Word &x, const Word &y) {
  return (x.freq > y.freq);
}

int main() {
  int n;
  string s;
  while (cin >> n) {
    vector<string> L(n);
    for (int i = 0; i < n; ++i) {
      cin >> s;
      L[i] = s;
    }

    sort(L.begin(), L.end());

    vector<Word> ws;
    for (string w : L) {
      if (not ws.empty() and ws[ws.size() - 1].word == w) {
        ws[ws.size() - 1].freq += 1;
      } else {
        Word w1 = {w, 1};
        ws.push_back(w1);
      }
    }

    sort(ws.begin(), ws.end(), customCompare);
    for (Word asa : ws) {
      cout << asa.freq << " " << asa.word << endl;
    }
    cout << "----------" << endl;
  }
}
