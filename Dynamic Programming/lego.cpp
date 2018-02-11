#include <iostream>
#include <vector>
using namespace std;
long long int power(long long int w,int h)
{
  long long int result = 1;
  long long int k = w;
  while(h)
  {
    if ((h % 2) == 1)
    {
      result = ((result % 1000000007) * (k% 1000000007)) % 1000000007;
    }
    h = h/2;
    k = ((k % 1000000007) * (k % 1000000007)) % 1000000007;
  }
  return result;
}
int main()
{
  int t;
  cin>>t;
  while(t--)
  {
  int width;
  int height;

  long long int temp_sol = 0;
  long long int result = 0;
  long long int tot = 0;
  long long int temp = 0;
  long long int sum = 1;
  long long int natemp = 0;
  long long int tempsol = 0;
  long long int finval = 0;
  vector<long long int> m;
  vector<long long int> s;
  vector<long long int> na;
  vector<long long int> a;



  cin>>height>>width;

  //Initialize m (table for memoization) for block width 1,2,3 & 4
  m.push_back(1);
  a.push_back(1);

  m.push_back(2);
  temp = power(2,height);
  a.push_back(temp);


  m.push_back(4);
  temp = power(4,height);
  a.push_back(temp);

  m.push_back(8);
  temp = power(8,height);
  a.push_back(temp);

  s.push_back(1);

  for(int i = 4;i <= width-1; i++)
  {
    tot = (m[i-1] % 1000000007 + m[i-2] % 1000000007 + m[i-3] % 1000000007 + m[i-4] % 1000000007) % 1000000007;
    m.push_back(tot);
    temp = power(tot,height);
    a.push_back(temp);
  }


  for(int j = 0; j <= width-2 ; j++)
  {
      if (j>0)
      {
        long int sum = 0;
        for(int k = 0; k <= j-1; k++ )
        {
          sum = ((sum%1000000007) + ((a[j-k-1] % 1000000007) * (s[k] % 1000000007)) % 1000000007) % 1000000007;
        }
        sum = a[j] - sum;
        s.push_back(sum);
        sum = (sum % 1000000007 * a[width - j - 2] % 1000000007) % 1000000007;
        sum = (sum % 1000000007 + na[j-1] % 1000000007) % 1000000007;
        na.push_back(sum);
      }
      else
        {
          natemp = ((s[j] % 1000000007) * (a[width - j - 2] % 1000000007)) % 1000000007;
          na.push_back(natemp);
      }
  }


  if (width == 1)
  {
      result = 1;
  }
  else
  {
    result = a[width-1] - na[width-2];
  }


  if (result < 0)
  {
    result = 1000000007 + result;
  }
  cout << result % 1000000007 << '\n';
}


  return 0;
}
