#include<iostream>
#include<vector>
#include<stack>

using namespace std;
std::stack<int> lower;
std::stack<int> sta;
std::stack<int> tmpvec;
int main()
{
  int nodes,edge;
  int frm,to;
  cin>>nodes>>edge;
  int prev[nodes + 1];
  int weight[nodes + 1];
  int curr;
  int pushflg;
  int temp;
  int edgcnt = 0;
  int levsize;
  int prevnode;
  bool calcdone[nodes + 1];
  bool visited[nodes+1];
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
    //std::cout << frm << to << '\n';
    prev[frm] = to;
  }

  prev[1] = 0;
  //prev[0] = -1;
  //logic to calc size of sub trees using DFS
  sta.push(1);
  visited[1] = 1;
  while(!sta.empty())
  {
    curr = sta.top();
    sta.pop();
    visited[curr] = 1;
    pushflg = 0;
    for(int i = 1 ; i < nodes + 1; i++)
    {
      if(adjmat[curr][i] == 1)
      {
        if(visited[i] == 0)
        {
          sta.push(i);
          pushflg = 1;
        }
        }
      }


    if (pushflg == 0)
    {
      lower.push(curr);
    }
  }
  for (int i = 1;i < nodes+1;i++)
  {
    visited[i] = 0;
    calcdone[i] = 0;
  }
  while(lower.size() != 0 )
  {
  levsize = lower.size();

  for (int i = 1; i < levsize + 1; i++)
  {
    temp = lower.top();
    lower.pop();
    weight[prev[temp]] = weight[temp] + weight[prev[temp]];
    calcdone[temp] = 1;
    //std::cout << temp << '\n';
    //for(int l = 0;l<nodes+1;l++)
    //{
    //  std::cout << weight[l] << ' ';
    //}
    //std::cout << temp << '\n';

    //+visited[temp] = 1;
    prevnode = prev[temp];
    while(calcdone[prevnode] == 1 && prevnode != 0)
    {
      prevnode = prev[prevnode];
      if (prevnode == 0)
      {
        break;
      }
      std::cout << prevnode << ' '<< temp<<'\n';
      weight[prevnode] = weight[prevnode] + weight[temp];
    }
    if (visited[prev[temp]] == 0)
    {
      if(temp != 1)
      {
        tmpvec.push(prev[temp]);
        visited[prev[temp]] = 1;
      }

    }
  }
    lower = tmpvec;
    tmpvec = std::stack<int>();
  }

  for (int j = 2; j < nodes + 1 ; j++)
  {
    if (weight[j] % 2 == 0)
    {
      edgcnt++;
    }
  }
  std::cout << edgcnt << '\n';

  return 0;

}
