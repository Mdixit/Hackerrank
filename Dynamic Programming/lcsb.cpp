/* Longest common subsequence using Binary Search */
#include <bits/stdc++.h>

using namespace std;

int longestIncreasingSubsequence(vector <int> arr) 
{
    int len = arr.size();
    vector <int> alist;
    int max = 1;
    int found = 0;
    int idx = int(len/2);
    alist.push_back(arr[0]); 
    for (int i = 1; i < len; i++)
    {
        if(arr[i] > alist[alist.size() - 1])
        {
            alist.push_back(arr[i]);
            max++;
            continue;
        }

        else if(arr[i] <= alist[0])
        {
            alist[0] = arr[i];
            continue;
        }

        else
        {
            int mid = int(alist.size() / 2);
            int begin = 0;
            int end = alist.size() - 1;
            int found = 0;
            while(found == 0)
            {
                if (alist[mid] == arr[i])
                {
                    found = 1;
                    continue;
                }
                if(alist[mid] < arr[i])
                {
                    begin = mid + 1;
                }
                else if (alist[mid] > arr[i])
                {
                    end = mid;
                }

                if (begin == end)
                {
                    alist[begin] = arr[i];
                    found = 1;
                    continue;
                }
                mid = int((begin + end ) / 2);
            }
        
        }
        


    }
    
    return max;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    int result = longestIncreasingSubsequence(arr);
    cout << result << endl;
    return 0;
}
