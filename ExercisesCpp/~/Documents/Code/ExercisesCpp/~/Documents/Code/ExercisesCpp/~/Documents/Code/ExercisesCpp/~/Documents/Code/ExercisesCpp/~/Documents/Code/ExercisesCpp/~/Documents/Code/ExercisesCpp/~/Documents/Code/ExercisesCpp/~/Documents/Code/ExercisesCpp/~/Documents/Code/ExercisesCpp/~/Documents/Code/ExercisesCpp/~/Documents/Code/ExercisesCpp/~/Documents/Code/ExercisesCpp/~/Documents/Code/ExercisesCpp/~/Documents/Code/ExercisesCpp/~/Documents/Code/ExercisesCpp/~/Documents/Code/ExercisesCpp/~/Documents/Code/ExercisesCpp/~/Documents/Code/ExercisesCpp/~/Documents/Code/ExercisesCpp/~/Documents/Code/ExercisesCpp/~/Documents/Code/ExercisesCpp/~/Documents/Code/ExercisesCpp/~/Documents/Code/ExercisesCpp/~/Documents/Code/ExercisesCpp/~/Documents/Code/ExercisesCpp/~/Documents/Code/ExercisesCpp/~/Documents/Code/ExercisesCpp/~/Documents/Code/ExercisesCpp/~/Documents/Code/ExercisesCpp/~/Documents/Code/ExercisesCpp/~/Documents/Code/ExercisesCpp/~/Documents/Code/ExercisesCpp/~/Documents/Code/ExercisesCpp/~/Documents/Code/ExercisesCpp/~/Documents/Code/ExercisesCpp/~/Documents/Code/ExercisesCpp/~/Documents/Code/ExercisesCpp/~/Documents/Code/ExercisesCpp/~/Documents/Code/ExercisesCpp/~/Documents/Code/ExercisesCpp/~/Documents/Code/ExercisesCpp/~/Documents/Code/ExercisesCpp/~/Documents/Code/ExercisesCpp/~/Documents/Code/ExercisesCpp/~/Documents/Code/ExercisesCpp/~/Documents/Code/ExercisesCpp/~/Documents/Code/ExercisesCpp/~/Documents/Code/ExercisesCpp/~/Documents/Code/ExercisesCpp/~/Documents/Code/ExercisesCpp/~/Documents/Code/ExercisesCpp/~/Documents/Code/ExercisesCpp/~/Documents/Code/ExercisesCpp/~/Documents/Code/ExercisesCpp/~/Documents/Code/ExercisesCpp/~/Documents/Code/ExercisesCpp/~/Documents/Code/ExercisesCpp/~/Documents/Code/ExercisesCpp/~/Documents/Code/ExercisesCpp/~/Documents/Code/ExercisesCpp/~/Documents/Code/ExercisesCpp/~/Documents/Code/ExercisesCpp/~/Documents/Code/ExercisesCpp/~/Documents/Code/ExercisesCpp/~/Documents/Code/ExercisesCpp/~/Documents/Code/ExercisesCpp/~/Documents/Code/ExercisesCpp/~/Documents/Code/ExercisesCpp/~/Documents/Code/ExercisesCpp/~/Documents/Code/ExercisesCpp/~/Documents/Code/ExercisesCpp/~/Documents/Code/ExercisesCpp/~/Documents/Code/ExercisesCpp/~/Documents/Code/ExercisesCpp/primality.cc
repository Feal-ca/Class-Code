#include <iostream>
using namespace std;

bool es_primer(int n) {
    if (n <= 1) return false;
    
    for (int i = 2; i*i <= n; ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main(){
    int n, a;
    cin >> n;

    for (int i = 0; i < n; ++i){
        cin >> a;
        cout << a << " is ";
        if (!es_primer(a)){
            cout << "not ";
        }
        cout << "prime" << endl;
        
    }
    

}