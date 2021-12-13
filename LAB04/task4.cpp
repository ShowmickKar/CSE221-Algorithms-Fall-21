#include <bits/stdc++.h>
#define inf 1e5;
using namespace std;

int n, m;

vector<vector<pair<int, int>>> adj(101);
vector<vector<int>> paths(101);

int find_length(int u, int v) {
    for (auto &x : adj[u]) {
        if (x.first == v) {
            return x.second;
        }
    }
    return 0;
}

void traverse(int c, int s) {
    if (c != s) {
        for (auto &u : paths[s]) {
            paths[c].push_back(min(u, find_length(s, c)));
        }
    }
    for (auto &u : adj[c]) {
        traverse(u.first, c);
    }
}

int main() {
    freopen("tests/input-task4.txt", "r", stdin);
    freopen("tests/output-task4.txt", "w", stdout);

    int t;
    cin >> t;
    while(t--) {
        cin >> n >> m;
        while(m--) {
            int u, v, w;
            cin >> u >> v >> w;
            adj[u].push_back({v, w});            
        }
        int s;
        cin >> s;
        paths[s].push_back(1000);
        traverse(s, s);
        for (int i = 1; i <= n; i++) {
            if (i == s) {
                cout << 0 << " ";
            } else {
                int ans = 0;
                for (auto &u : paths[i]) {
                    ans = max(ans, u);
                }
                cout << (ans == 0 ? -1 : ans) << " ";
            }
        }
        cout << endl;

        for (int i = 0; i < adj.size(); i++) {
            adj[i].clear();
            paths[i].clear();
        }
    }
}