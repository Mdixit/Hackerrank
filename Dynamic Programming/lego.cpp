#include <stdio>
#include <vector>
int main()
{
  int width;
  int height;
  long int temp_sol;
  long int result
  vector<long int> m;
  vector<long int> s;
  vector<long int> a;
  //Initialize m (table for memoization) for block width 1,2,3 & 4
  m.push_back(1);
  a.push_back(1^h);

  m.push_back(2);
  a.push_back((2^h) % 1000000007);


  m.push_back(4);
  a.push_back((4^h) % 1000000007);

  m.push_back(8);
  a.push_back((8^h) % 1000000007);

  s.push_back(1);

  cin>>height>>width;

  for(int i = 5;i <= width; i++)
  {
    tot = (m[i-1] + m[i-2] + m[i-3] + m[i-4]) % 1000000007;
    m.push_back(tot);
    a.push_back((tot^h) % 1000000007);
  }


  for(int j = 1; j < width ; j++)
  {
      temp_sol = (a[j] - (s[j-1] * (m[width-j]^height))) % 1000000007;
      if (j > 1)
      {
        s.push_back((s[j-1] + temp_sol) % 1000000007);
      }
      else
      {
        s.push_back(temp_sol);
      }
  }

  result = s[width-1];
  cout << result << '\n'
  return 0;
}
