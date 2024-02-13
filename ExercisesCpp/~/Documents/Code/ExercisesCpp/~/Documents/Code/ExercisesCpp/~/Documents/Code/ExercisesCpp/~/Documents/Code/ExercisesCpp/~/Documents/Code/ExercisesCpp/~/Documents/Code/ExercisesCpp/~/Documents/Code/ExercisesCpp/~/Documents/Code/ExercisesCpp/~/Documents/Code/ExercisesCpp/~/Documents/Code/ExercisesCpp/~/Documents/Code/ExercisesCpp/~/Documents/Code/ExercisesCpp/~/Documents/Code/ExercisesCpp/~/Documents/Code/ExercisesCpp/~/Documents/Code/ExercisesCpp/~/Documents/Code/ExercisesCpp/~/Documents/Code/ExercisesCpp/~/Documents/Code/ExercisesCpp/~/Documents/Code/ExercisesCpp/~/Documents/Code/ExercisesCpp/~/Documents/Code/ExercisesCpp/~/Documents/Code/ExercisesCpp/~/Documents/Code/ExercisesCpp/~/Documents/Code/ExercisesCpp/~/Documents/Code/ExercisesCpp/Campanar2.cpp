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
    campanadas = campanadas + 22*(t/1440);
    t = t%1440;

    for (int i = 0; i < t; i++) {
      int h_mod = h%12;
      double m_angle = (2*numbers::pi)/60.0 * m;
      double h_angle = ((2*numbers::pi)/12.0 * h_mod) + (m_angle)/12.0;
        
      if (abs(h_angle - m_angle) < 0.01){
        ++campanadas;
      }
      mas_un_minuto(h,m);
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
      if(h_mod == 3 && m == 15){
        ++campanadas;
      }
      if (h_mod == 4 && m == 20) {
        
      }
      if(h_mod == 5 && m == 25){
        ++campanadas;
      }
      if(h_mod == 6 && m == 30){
        ++campanadas;
      }
      if(h_mod == 7 && m == 35){
        ++campanadas;
      }
      if(h_mod == 8 && m == 40){
        ++campanadas;
      }
      if(h_mod == 9 && m == 45){
        ++campanadas;
      }
      if(h_mod == 10 && m == 50){
        ++campanadas;
      }*/

