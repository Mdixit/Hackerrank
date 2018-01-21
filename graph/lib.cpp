#include <iostream>
#include <vector>
#include<stack>
using namespace std;
int t,city,path,clib,croad,frm,to;
std::stack<int> nodes;
/*int dfs(int s,bool visit)
{
    int count = 1,curr;
    nodes.push_back(s);
    while (!nodes.empty())
    {
        count++ ;
        curr = nodes.pop_back();
        visit[curr] = true;
        for (int i = 0; i < adj[curr].len(),i++)
        {
          nodes.push_back(adj[curr][i])
        }
    }
    return count;
}*/
int main()
{

  cin>>t;
  long int cost = 0;
  int count,curr;
  while(t--)
  {
    cin>>city>>path>>clib>>croad;
    bool visited[city+1];
    std::vector<int> adj[city+1];
    cost = 0;
    while(path--)
    {
      cin>>frm>>to;
      adj[frm].push_back(to);
      adj[to].push_back(frm);

    }
    for (int i = 1;i <= city;i++)
    {
      visited[i] = false;
    }
    for (int i = 1; i <= city ; i++)
    {
      if (visited[i] == false)
      {
        count = 0;
        nodes.push(i);
        visited[i] = true;
        while (!nodes.empty())
        {
            count++ ;
            curr = nodes.top();
            nodes.pop();
            //visited[curr] = true;
            for (int k = 0; k < adj[curr].size();k++)
            {
              if (visited[adj[curr][k]] != true)
              {
                nodes.push(adj[curr][k]);
                visited[adj[curr][k]] = true;
              }
            }
        }

        if (count == 1)
        {
          cost += clib;
        }
        else
        {
          if (croad > clib)
          {
            cost += clib * count;
          }
          else
          {
            cost += ((count-1) * croad) + clib;
          }
        }
      }
    }
    std::cout <<cost<< '\n';
  }

  return 0;
}
