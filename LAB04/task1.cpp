#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> adj(101);
vector<bool> visited(101);
vector<int> dist(101);
vector<int> parent(101);

int n, m;


void dijkstra(int x) {
    for (int i = 1; i <= n; i++) dist[i] = 1e5+1;
    dist[x] = 0;
    priority_queue<pair<int, int>> q;
    q.push({0, x});
    while(!q.empty()) {
        int p = q.top().second;
        q.pop();
        if (visited[p]) continue;
        visited[p] = true;
        for (auto &u : adj[p]) {            
            int b = u.first;
            int w = u.second;          
            if (dist[p] + w < dist[b]) {
                dist[b] = dist[p] + w;
                q.push({-dist[b], b});
            }
        } 
    }
}

int main() {
    freopen("tests/input-task1.txt", "r", stdin);
    freopen("tests/output-task1.txt", "w", stdout);

    int t; 
    cin >> t;
    while(t--) {
        cin >> n >> m;
        while (m--) {
            int u, v, w;
            cin >> u >> v >> w;
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        dijkstra(1);
        cout << dist[n] << endl;
        for (int i = 0; i < adj.size(); i++) {
            adj[i].clear();
            visited[i] = false;
            dist[i] = 0;
            parent[i] = 0;
        }
    }
}