#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, X, inp, index = 0;
    int arr[10004];
    cin >> N >> X;
    for(int i = 0; i < N;i++){
      cin >> inp;
      if(X > inp){
        arr[index] = inp;
        index++;
      }
      
    }
    for(int i = 0; i < index;i++){
      cout << arr[i] << " ";
      }
    return 0;
}