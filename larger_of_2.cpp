/* finding larger of two numbers */
#include<iostream>
using namespace std;

int main(void) {
    /* The two numbers */
    int number1, number2;

    /* Store Larger Number */
    int max;

    /* Read two numbers */

    cin >> number1;
    cin >> number2;

    max = number1;

    if(number1 > max)
        max = number2;
    
    cout << "The larger number is " << max << endl;

    return 0;

}