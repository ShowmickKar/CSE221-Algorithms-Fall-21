#include <bits/stdc++.h>
using namespace std;

void execute(string input_file, string output_file) {
    freopen(input_file.c_str(), "r", stdin);
    freopen(output_file.c_str(), "w", stdout);

    int n; cin >> n;
    vector<pair<int, int>> times(n);
    for (auto &u : times) {
        cin >> u.second >> u.first;
    }
    sort(times.begin(), times.end());
    vector<pair<int, int>> ans;
    int prev = -1;
    for (int i = 0; i < n; i++) {
        if (times[i].second >= prev) {
            ans.push_back({times[i].second, times[i].first});
            prev = times[i].first;
        }
    }
    cout << ans.size() << endl;
    for (auto &u : ans) {
        cout << u.first << " " << u.second << endl;
    }
}

int main() {
    execute("task1-input1.txt", "task1-output1.txt");
    execute("task1-input2.txt", "task1-output2.txt");
}