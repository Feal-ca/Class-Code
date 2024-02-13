#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

string getAminoAcid(const string codon) {
  static const unordered_map<string, string> codonToAmino = {
      {"AUG", "Met"}, {"UUU", "Phe"}, {"UUC", "Phe"}, {"UUA", "Leu"},
      {"UUG", "Leu"}, {"UCU", "Ser"}, {"UCC", "Ser"}, {"UCA", "Ser"},
      {"UCG", "Ser"}, {"UAU", "Tyr"}, {"UAC", "Tyr"}, {"UGU", "Cys"},
      {"UGC", "Cys"}, {"UGG", "Trp"}, {"CUU", "Leu"}, {"CUC", "Leu"},
      {"CUA", "Leu"}, {"CUG", "Leu"}, {"CCU", "Pro"}, {"CCC", "Pro"},
      {"CCA", "Pro"}, {"CCG", "Pro"}, {"CAU", "His"}, {"CAC", "His"},
      {"CAA", "Gln"}, {"CAG", "Gln"}, {"CGU", "Arg"}, {"CGC", "Arg"},
      {"CGA", "Arg"}, {"CGG", "Arg"}, {"AUU", "Ile"}, {"AUC", "Ile"},
      {"AUA", "Ile"}, {"ACU", "Thr"}, {"ACC", "Thr"}, {"ACA", "Thr"},
      {"ACG", "Thr"}, {"AAU", "Asn"}, {"AAC", "Asn"}, {"AAA", "Lys"},
      {"AAG", "Lys"}, {"AGU", "Ser"}, {"AGC", "Ser"}, {"AGA", "Arg"},
      {"AGG", "Arg"}, {"GUU", "Val"}, {"GUC", "Val"}, {"GUA", "Val"},
      {"GUG", "Val"}, {"GCU", "Ala"}, {"GCC", "Ala"}, {"GCA", "Ala"},
      {"GCG", "Ala"}, {"GAU", "Asp"}, {"GAC", "Asp"}, {"GAA", "Glu"},
      {"GAG", "Glu"}, {"GGU", "Gly"}, {"GGC", "Gly"}, {"GGA", "Gly"},
      {"GGG", "Gly"}, {"UAA", "STP"}, {"UAG", "STP"}, {"UGA", "STP"}};

  auto it = codonToAmino.find(codon);
  if (it != codonToAmino.end()) {
    return it->second;
  } else {
    return "Unknown";
  }
}

string clear_useless_stuff(string RNA) {
  for (int i = 0; i < RNA.size(); ++i) {
    if (RNA[i] == 'A') {
      if (RNA[i + 1] == 'U') {
        if (RNA[i + 2] == 'G') {
          return RNA.erase(0, i + 3);
        }
      }
    }
  }
  return RNA;
}
int main() {
  int count = 1;
  string title = " ";
  string input;
  string RNA = "";
  string amino = "";
  while (title.back() != ':') {
    cin >> title;
  }
  while (cin >> input) {
    RNA += input;
  }

  RNA = clear_useless_stuff(RNA);

  int n_codons = RNA.size() / 3;
  for (int i = 0; i <= n_codons; ++i) {
    amino = getAminoAcid(RNA.substr(0, 3));
    if (amino != "STP") {

      // cout << RNA.substr(0, 3) << ": " << amino << endl;
      cout << amino;

      if (count == 26) {
        cout << endl;
        count = 0;
      }
      RNA.erase(0, 3);
      count += 1;
    } else {
      cout << endl;
      break;
    }
  }
}
