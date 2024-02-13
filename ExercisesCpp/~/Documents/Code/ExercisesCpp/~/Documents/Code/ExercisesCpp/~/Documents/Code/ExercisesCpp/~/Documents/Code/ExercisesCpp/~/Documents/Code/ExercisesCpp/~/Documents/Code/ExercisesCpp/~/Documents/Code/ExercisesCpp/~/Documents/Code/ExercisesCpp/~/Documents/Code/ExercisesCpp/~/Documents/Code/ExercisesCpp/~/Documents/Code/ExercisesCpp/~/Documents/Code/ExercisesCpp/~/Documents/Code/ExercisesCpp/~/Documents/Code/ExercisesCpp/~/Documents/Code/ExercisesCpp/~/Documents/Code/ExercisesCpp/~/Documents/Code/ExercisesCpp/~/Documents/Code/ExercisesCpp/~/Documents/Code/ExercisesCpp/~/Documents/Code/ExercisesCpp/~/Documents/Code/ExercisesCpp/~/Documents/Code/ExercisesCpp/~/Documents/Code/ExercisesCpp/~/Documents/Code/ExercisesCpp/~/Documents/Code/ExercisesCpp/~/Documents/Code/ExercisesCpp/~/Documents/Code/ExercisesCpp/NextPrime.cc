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
    int a;

    while (cin>>a){
        if(!es_primer(a)) break;
        
        ++a;

        while (!es_primer(a)){
            ++a;
        }
        
        cout << a << endl;
        
    }
    

}