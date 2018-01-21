#include <iostream>
#include <vector>
#include<stack>
using namespace std;
int city,path,frm,to;
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

  //cin>>t;
  long int cost = 0;
  int count,curr,node;
  //while(t--)
  //{
    cin>>node>>path;
    bool visited[node];
    std::vector<int> adj[node];
    std::vector<int> comps;
    cost = 0;
    int sum = 0;
    while(path--)
    {
      cin>>frm>>to;
      adj[frm].push_back(to);
      adj[to].push_back(frm);

    }
    for (int i = 0;i < node;i++)
    {
      visited[i] = false;
    }
    for (int i = 0; i < node ; i++)
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

        comps.push_back(count);
        sum += count;
      }
    }
    for (int l = 0 ; l < comps.size();l++)
    {
      cost += comps[l] * (sum - comps[l]);
    }
    cost = cost / 2;
    std::cout <<cost<< '\n';
  //}

  return 0;
}
