#include <bits/stdc++.h>

using namespace std;

vector <int> longestCommonSubsequence(vector <int> a, vector <int> b) 
{
    int n = a.size();
    int m = b.size();
    int dp[n+1][m+1];
    vector<int> seq;
    for(int i = 0; i <= n; i++)
    {
        dp[i][0] = 0;
    }
    for(int i = 0; i <= m; i++)
    {
        dp[0][i] = 0;
    }

    for(int itr = 0; itr < n ; itr++)
    {
        for(int i_itr = 0; i_itr < m ; i_itr++)
        {
            if (a[itr] == b[i_itr])
            {
                dp[itr + 1][i_itr + 1] = dp[itr][i_itr] + 1;
            }
            else
            {
                if (dp[itr][i_itr+1] >= dp[itr + 1][i_itr])
                {
                    dp[itr + 1][i_itr + 1] = dp[itr][i_itr + 1];
                }
                else
                {
                    dp[itr + 1][i_itr + 1] = dp[itr + 1][i_itr];
                }
            }
        }
    }
    int i = n;
    int j = m;
    while(i != 0 && dp[i][j] != 0)
    {
        if(dp[i][j] == dp[i][j-1])
        {
            j = j-1;
            continue;
        }
        
        if(dp[i][j] == dp[i-1][j])
        {
            i = i - 1;
            continue;
        }

        if(dp[i][j] == (dp[i-1][j-1] + 1))
        {
            seq.push_back(b[j-1]);
            j = j - 1;
            i = i - 1;
        }
        else
        {
            j = j - 1;
        }
    
    }
    std::reverse(seq.begin(),seq.end());
    return seq;
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
       cin >> a[a_i];
    }
    vector<int> b(m);
    for(int b_i = 0; b_i < m; b_i++){
       cin >> b[b_i];
    }
    vector <int> result ;
    result = longestCommonSubsequence(a, b);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? " " : "");
    }
    cout << endl;


    return 0;
}
