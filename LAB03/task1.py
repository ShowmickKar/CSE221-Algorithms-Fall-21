def build_graph(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph
