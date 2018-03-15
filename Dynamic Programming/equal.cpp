#include <bits/stdc++.h>

using namespace std;

int equal(vector <int> arr) {
    int min = 0;
    int min1;
    int min3;
    int min5;
    for(int i = 0; i < arr.size();i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    min1 = min - 1;
    min3 = min - 3;
    min5 = min - 5;

    if (!(min >= 0))
        {
            min = 0;    
        }
    for(int j = 0; j < arr.size() ;j++)
    { 
        int diff = 0;
        int stp5 = 0;
        int stp3 = 0;
        int stp1 = 0;
        int minsteps = 0;
        int min1steps = 0;
        int min3steps = 0;
        int min5steps = 0;
        diff = arr[j] - min;
        if (diff != 0)
        {
            minsteps += calc_stp(arr[j],diff);
        }
        
        diff = arr[j] - min1;
        if(diff != 0 && min1 > 0)
        {
            min1steps += calc_stp(arr[j],diff);
        }
        
        diff = arr[j] - min3;
        if(diff != 0 && min3 > 0)
        {
            min3steps += calc_stp(arr[j],diff);
        }
        
        diff = arr[j] - min3;
        if(diff != 0 && min3 > 0)
        {
            min5steps += calc_stp(arr[j],diff);
        }    
    }

}

int calc_stp(int elem,int differ)
{
    
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int arr_i = 0; arr_i < n; arr_i++){
           cin >> arr[arr_i];
        }
        int result = equal(arr);
        cout << result << endl;
    }
    return 0;
}
