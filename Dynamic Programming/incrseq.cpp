/* Longest common subsequence using DP */
#include <bits/stdc++.h>

using namespace std;

int longestIncreasingSubsequence(vector <int> arr) {
    int len = arr.size();
    int dp[len];
    int max = 0;
    for(int i = 0; i < len; i++)
    {
        dp[i] = 1;
    }
    for(int i = 1; i < len; i++)
    {
        for(int j = 0; j < i; j++)
        {
            if ((arr[i] > arr[j]) && (dp[i] <= dp[j]))
            {
                dp[i] = dp[j] + 1;
                if (max < dp[i])
                {
                    max = dp[i];
                }
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
