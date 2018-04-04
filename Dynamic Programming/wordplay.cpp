#include <bits/stdc++.h>
#include<iostream>
#include<cstring>
#include<string.h>
#include<vector>
#include<array>
#include<algorithm>
using namespace std;

/*
 * Complete the playWithWords function below.
 */
int playWithWords(string s) 
{
    int res = 0;
    int len = s.length();
    int dp[3][len];
    int maxprd = 0;
    int temprd;
    int temp[len];
    int start[len];
    int end[len];

    start[0] = 1;
    end[0] = 0;
    end[len - 1] = 1;
    for (int itr = 0; itr < len; itr++) //init dp array
    {
        dp[1][itr] = 1;
        dp[0][itr] = 0;
    }
    
    for(int chain = 2; chain <= len; chain++)
    {
        for(int itr = 0; itr < len - chain + 1; itr++)
        {   
            if(s[itr] == s[itr + chain - 1])
            {
                dp[2][itr + chain - 1] = dp[0][itr + chain - 2] + 2;
            }
            else
            {
                if ((dp[1][itr + chain - 2]) >= (dp[1][itr + chain - 1]))
                { 
                    dp[2][itr + chain - 1] = dp[1][itr + chain - 2];
                }
                else
                {
                    dp[2][itr + chain - 1] = dp[1][itr + chain - 1];
                }
            }
        }
        
        start[chain - 1] = dp[2][chain - 1];
        end[chain - 1] = dp[2][len - 1];

        for(int l = 0; l < len; l++)
        {            
            dp[0][l] = dp[1][l];
            dp[1][l] = dp[2][l];
        }


    }

    for (int itr = 0; itr < len - 1; itr++)
    {
        temprd = start[itr] * end[len - itr - 2];
        if (maxprd < temprd)
        {
            maxprd = temprd;
        }
    }
    return maxprd;
 
}

int main()
{
    //ofstream fout(getenv("OUTPUT_PATH"));

    string s ;
    getline(cin, s);

    int result = playWithWords(s);
    cout << result << "\n";
    //fout << result << "\n";

    //fout.close();

    return 0;
}
