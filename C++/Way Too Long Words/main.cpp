#include<iostream>

using namespace std;


int main() {
    
    int i;
    cin >> i;
    int count = i;

    while (count != 0) {

        string w;
        cin >> w;
        int l = w.length();
        if (l <= i) {
            cout << w << endl;
            count--;
        } else {
            cout << "test" << endl;
            string sub = w.substr(1, l-1);
            int sl = sub.length();
            cout << w[0] + sl + w[l+1] << endl; 
            count--;

        }





    }


    return 0;



}