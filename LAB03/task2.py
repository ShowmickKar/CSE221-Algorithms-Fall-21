import math
from queue import Queue
from file_io import read, write
from task1 import build_graph


def breadth_first_search(start, target, visited, path):
    visited[start] = True
    q = Queue()
    q.put(start)
    while not q.empty():
        s = q.get()
        path.append(s)
        if s == target:
            return
        for x in graph[s]:
            if visited[x]:
                continue
            visited[x] = True
            q.put(x)


n, m, edges = read()
graph = build_graph(n, m, edges)
visited = [False for _ in range(n + 1)]
path = []
breadth_first_search(1, 12, visited, path)
print(path)
write("task2_output.txt", path)
