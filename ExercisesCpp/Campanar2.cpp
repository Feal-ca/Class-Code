#include <iostream>
#include <cmath>
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
    //11 veces cada vuelta entera
    int campanadas = 0;
    campanadas = campanadas + 11*(t/720);
    t = t%720;

    for (int i = 0; i < t; i++) {
      int h_mod = h%12;
        
      if (m*11 <= 60*h_mod && 11*(m+t)> 60*h_mod){
        ++campanadas;
      }
      t = t - 60 + m;
      m = 0;
      ++h;
      if (h==12) {
        h = 1;
        t -= 60;
      }
    }
  cout << campanadas << endl;
  }
}

/*
12 00
01 05
02 10
03 15
04 20
05 25
06 30
07 35
08 40
09 45
10 50
*/ 
/*if(h_mod == 0 && m == 0){
        ++campanadas;
      }
      if(h_mod == 1 && m == 5){
        ++campanadas;
      }
      if(h_mod == 2 && m == 10){
        ++campanadas;
      }
      if(h_mod == 3 && m == 16){
        ++campanadas;
      }
      if (h_mod == 4 && m == 21) {
        
      }
      if(h_mod == 5 && m == 27){
        ++campanadas;
      }
      if(h_mod == 6 && m == 32){
        ++campanadas;
      }
      if(h_mod == 7 && m == 38){
        ++campanadas;
      }
      if(h_mod == 8 && m == 43){
        ++campanadas;
      }
      if(h_mod == 9 && m == 49){
        ++campanadas;
      }
      if(h_mod == 10 && m == 54){
        ++campanadas;
      }*/

