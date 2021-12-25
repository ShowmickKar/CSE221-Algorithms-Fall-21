#include <bits/stdc++.h>
using namespace std;

void execute(string input_file, string output_file) {
    freopen(input_file.c_str(), "r", stdin);
    freopen(output_file.c_str(), "w", stdout);

    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> times(n);
    for (auto &u : times) {
        cin >> u.second >> u.first;
    }
    sort(times.begin(), times.end());
    multiset<int> prev;
    for(int i = 0; i < m; i++) {
        prev.insert(0);
    }
    int counter = 0;
    for (auto &u : times) {
        for (auto &p :  prev) {
            if (u.second >= p) {
                prev.erase(prev.lower_bound(p));
                prev.insert(u.first);
                counter++;
                break;
            }
        }
    }    
    cout << counter << endl;
}  

int main() {
    execute("task2-input1.txt", "task2-output1.txt");
    execute("task2-input2.txt", "task2-output2.txt");
}