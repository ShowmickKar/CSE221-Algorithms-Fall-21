#include <bits/stdc++.h>
using namespace std;

void execute(string input_file, string output_file) {
    freopen(input_file.c_str(), "r", stdin);
    freopen(output_file.c_str(), "w", stdout);

    int n, jack_time = 0, jill_time = 0;
    cin >> n;
    vector<int> times(n);
    for (auto &u : times) {
        cin >> u;
    }
    sort(times.begin(), times.end());
    string turn, sequence = "";
    cin >> turn;
    queue<int> q;
    stack<int> s;
    for (auto &t : times) {
        q.push(t);
    }
    for (int i = 0; i < turn.size(); i++) {
        if (turn[i] == 'J') {
            if (!q.empty()) {
                s.push(q.front());
                jack_time += q.front();
                sequence += to_string(q.front());
                q.pop();                
            }
        } else {
            if (!s.empty()) {
                jill_time += s.top();
                sequence += to_string(s.top());
                s.pop();
            }
        }
    }
    cout << sequence << endl;
    cout << "Jack will work for " << jack_time << " hours\nJill will work for " << jill_time << " hours";
}

int main() {
    execute("task3-input1.txt", "task3-output1.txt");
    execute("task3-input2.txt", "task3-output2.txt");
}