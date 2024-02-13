#include <iostream>
#include <vector>
using namespace std;

void show_board(vector<vector<bool>> &board) {
  for (vector<bool> a : board) {
    for (bool b : a) {
      if (b) {
        cout << 'X';
      } else {
        cout << '.';
      }
    }

    cout << endl;
  }
  cout << endl;
}

void alfil_mov(vector<vector<bool>> &board) {
  int speed_x = -1;
  int speed_y = -1;

  int pos_x = 0;
  int pos_y = 0;

  while (not board[pos_y][pos_x] or (pos_y != 0 and pos_x != 0)) {
    board[pos_y][pos_x] = true;

    if (pos_y == board.size() - 1 or pos_y == 0) {
      speed_y = speed_y * -1;
    }
    if (pos_x == board[0].size() - 1 or pos_x == 0) {
      speed_x = speed_x * -1;
    }

    pos_x += speed_x;
    pos_y += speed_y;

    // cout << "Speed: " << speed_x << " : " << speed_y << endl << "Pos: " <<
    // pos_x << " : " << pos_y << endl
    // << endl;
  }
}

int main() {
  int f, c;

  while (cin >> f) {
    cin >> c;
    vector<vector<bool>> taulell(f, vector<bool>(c, false));
    alfil_mov(taulell);
    show_board(taulell);
  }
}
