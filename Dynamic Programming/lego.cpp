#include <stdio>
#include <vector>
int main()
{
  int width;
  int height;
  vector<int> m;
  vector<int> s;
  //Initialize m (table for memoization) for block width 1,2,3 & 4
  m.push_back(1);
  m.push_back(2);
  m.push_back(4);
  m.push_back(8);

  s.push_back(1);

  cin>>height>>width;

  for(int i = 5;i <= width; i++)
  {
    tot = m[i-1] + m[i-2] + m[i-3] + m[i-4];
    m.push_back(tot);
  }

  tot_ways = (m[width-1]^height) % 1000000007;

  //non-solid walls

  for(int j = 1; j < width ; j++)
  {
    all = (m[i-1]^h) % 1000000007;
    solid = all[i] - (m[i-1]*all[i-1]) % 1000000007;
    s.push_back(solid);
  }
  return 0;
}
