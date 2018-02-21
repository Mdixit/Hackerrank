#include<iostream>
#include<vector>
#include<stack>

using namespace std;
int main()
{
  int nodes,edge;
  int frm,to;
  int prev[nodes + 1];
  int weight[nodes + 1];
  int curr;
  std::stack<int> lower;
  bool visited[nodes+1];
  std::stack<int> sta;
  cin>>nodes>>edge;
  bool adjmat[nodes+1][nodes+1];

  for(int i = 0;i < nodes + 1; i++ )
  {
    for(int j = 0; j < nodes + 1; j++ )
    {
      adjmat[i][j] = 0 ;
    }
    weight[i] = 1;
    visited[i] = 0;
  }

  while(edge--)
  {
    cin>>frm>>to;
    adjmat[frm][to] = 1;
    adjmat[to][frm] = 1;
    prev[to] = frm;
  }

  prev[1] = 0;
  //logic to calc size of sub trees using DFS
  sta.push(1);
  visited[1] = 1;
  while(!sta.empty())
  {
    curr = sta.top();
    sta.pop();
    visited[curr] = 1;
    for(int i = 1 ; i < nodes; i++)
    {
      if(adjmat[curr][i] == 1)
      {
        if(visited[i] == 0)
        {
          sta.push(i);
          pushflg = 1
        }
      }
    }
    if (pushflg == 0)
    {
      lower.push(i);
    }
  }
  while(lower != 0)
  {
  for (i = 1; i <= lower.length(); i++)
  {
    temp = lower.pop_back();
    weight[prev[temp]] = weight[temp] + weight[prev[temp]];
    tmpvec.push_back(prev[temp]);
  }
    lower = tmpvec;
  }
  return 0;

}
