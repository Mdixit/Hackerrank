#include <bits/stdc++.h>

using namespace std;

void insertionSort2(int n, vector <int> arr) {
    int num;
    int temp;
    int shift = 0;
    bool insflag = false;
    for(int i = 1; i < n; i++)
    {   num = arr[i];
        insflag = false;
        for(int j = i - 1; j >= 0; j--)
        {
            if(arr[j] <= num)
            {
                arr[j+1] = num;
                insflag = true;
                for(int k=0; k<n; k++)
                {
                    cout<<arr[k]<<' ';
                }
                cout<<'\n';
                break;
            }
            else
            {
                arr[j+1] = arr[j];
                shift += 1;
            }
        }
        if (insflag == false)
        {
            arr[0] = num;
            for(int k=0; k<n; k++)
                {
                    cout<<arr[k]<<' ';
                }
                cout<<'\n';
        }
    }
      cout<<shift;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    insertionSort2(n, arr);
    return 0;
}
