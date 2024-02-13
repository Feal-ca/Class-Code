#include <iostream>
using namespace std;
// Define the struct
struct Position {
  // Member variables
  int x;
  int y;

  Position(int initialX, int initialY) : x(initialX), y(initialY) {}

  void update(int newX, int newY) {
    x = newX;
    y = newY;
  }
};

int main(){
  Position pos(1,3);
  cout << pos.x << endl;
  pos.update(3,6);
  cout << pos.x << endl;

}
