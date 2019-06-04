#include<iostream>
using namespace std;

int main(void){
    int i = 9, *p;

    p = &i;

    cout<<*p << endl;

    *p = 88;

    cout << i << endl;
}
