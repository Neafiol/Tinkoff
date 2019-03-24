#include "iostream"
#include "vector"
#include <cmath>

using namespace std;

int main(){
    vector<int> x;
    vector<int> y;
    x.push_back(4);
    y.push_back(5);

    x.push_back(0);
    y.push_back(-3);

    x.push_back(-1);
    y.push_back(-5);

    x.push_back(2);
    y.push_back(3);

    x.push_back(1);
    y.push_back(-5);

    x.push_back(-4);
    y.push_back(-2);

    x.push_back(3);
    y.push_back(1);

    x.push_back(4);
    y.push_back(5);

    x.push_back(1);
    y.push_back(5);

    x.push_back(1);
    y.push_back(0);

    double kn =0;
    double sum =0, now = 1e9;

    for (double i =0; i < 3.1416 ; i+=0.0001){
        double k=tan(i);
        sum =0;
        for (int j =0;j<10;j++){
            sum+=(y[j]-x[j]*k)*(y[j]-x[j]*k);
        }
        if (sum < now ){
            kn = k;
            now = sum;
        }
    }
    cout<<kn;
}