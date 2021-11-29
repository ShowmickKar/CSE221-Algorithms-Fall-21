from file_io import read, write
from task1 import build_graph


def depth_first_search(node, visited, target, path):
    visited[node] = True
    path.append(node)
    if node == target:
        return
    for child in graph[node]:
        if visited[target]:
            return
        if visited[child]:
            continue
        depth_first_search(child, visited, target, path)


n, m, edges = read()
graph = build_graph(n, m, edges)
visited = [False for _ in range(n + 1)]
path = []
depth_first_search(1, visited, 12, path)
print(path)
write("task3_output.txt", path)