#include <iostream>
using namespace std;

void mas_un_minuto(int& h, int& m){
  m += 1;
  if (m==60) {
    m = 0;
    h += 1;
    if (h == 24) {
      h = 0;
    }
  } 
}

int main(){
  int h,m,t;

  while(cin >> h >> m >> t){
    //484 veces cada dia entero
    //cin >> m >> s;
    int campanadas = 0;
    campanadas = campanadas + 484*(t/1440);
    t = t%1440;

    for (int i = 0; i < t; i++) {
      if(m == 0){
        campanadas += 4;
        if(h == 12) campanadas += 100;
        else if (h == 0) campanadas += 12;
        else campanadas += h%12;
      }
      if (m == 15) {
        campanadas += 1;
      }
      if (m == 30) {
        campanadas += 2;
      }
      if (m == 45) {
        campanadas += 3;
      }
      mas_un_minuto(h,m);
    }
  cout << campanadas << endl;
  }
}
