#include <iostream>
#include <vector>
#include<stack>
using namespace std;
int t,city,path,frm,to,curr;
int cnt;
std::stack<int> nodes;
int main()
{

  cin>>t;
  long int cost = 0;
  int s;
  while(t--)
  {
    cin>>city>>path;
    int path2 = path;
    bool visited[city+1];
    long int shrtpath[city+1];
    //std::vector<int> adj[city+1];
    bool adj[city+1][city+1];

    for(int i = 1 ; i < city + 1; i++)
    {
      for (int j = 1 ; j < city + 1 ; j++)
      {
        adj[i][j] = 0;
      }
    }
    //std::vector<int> prev[city+1];
    cost = 0;
    //convert to adj matrix
    while(path--)
    {
      cin>>frm>>to;
      adj[frm][to] = 1;
      adj[to][frm] = 1;
    }
    cin>>s;
    for (int i = 1;i <= city;i++)
    {
      visited[i] = false;
      shrtpath[i] = 2147483646;
    }
    shrtpath[s] = 0;
    nodes.push(s);
    visited[s] = true;

    while (!nodes.empty())
    {
        curr = nodes.top();
        nodes.pop();
        for (int k = 1; k < city + 1;k++)
        {
            if (adj[curr][k] == 1)
              {
                visited[k] = true;
                //prev.push_back(curr);
                if (shrtpath[k] > (shrtpath[curr] + 6) )
                {
                  shrtpath[k] = shrtpath[curr] + 6;
                  nodes.push(k);
                }
              }
        }
    }
  for (int j = 1;j<=city;j++)
  {
    if (j == s) continue;
    if (visited[j] == false)
    {
      std::cout << "-1";
    }
    else
    {
      std::cout << shrtpath[j];
    }
    cout<<' ';
  }
    cout<<'\n';
  }

  return 0;
}
