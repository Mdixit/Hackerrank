#include <bits/stdc++.h>

using namespace std;

long countArray(int n, int k, int x) 
{   int MOD = 1000000007;
    long dp00;
    long dp01; 
    long temp[2];
    dp00 = 1;
    dp01 = 0;
   /* 
    for(int iter = 1; iter < k ;iter++)
    {
        dp0[iter] = 0;
    }
    */
    for(int iter = 1; iter < (n-1); iter++)
    {
        for(int i_iter = 0; i_iter < 2; i_iter++)
        {
                if (i_iter == 0)
                {
                    temp[i_iter] = ( (dp00 + ( ( (k-1) * dp01 )  % MOD ) ) - dp00 ) % MOD;
                }
                else
                {
                    temp[i_iter] = ( (dp00 + ( ( (k-1) * dp01 )  % MOD ) ) - dp01 ) % MOD;
                }
        }   
           
        
        
        dp00 = temp[0];
        dp01 = temp[1];
    }
        
        //memcpy(dp0,dp1,sizeof(dp0)) ;
         
    if( x != 1)
    {
        return ( ( ( dp00 + ( ( ( k-1 ) * dp01 ) % MOD ) ) - dp01 ) % MOD )  ;
    }
    else
    {
        return ( ( ( dp00 + ( ( ( k-1 ) * dp01 ) % MOD ) ) - dp00 ) % MOD )  ;
    }
}

int main() {
    int n;
    int k;
    int x;
    cin >> n >> k >> x;
    long answer = countArray(n, k, x);
    cout << answer << endl;
    return 0;
}
