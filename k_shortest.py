from dijkstra import dijkstra
import copy

# simple k shortest path 
# uses dijkstra algo to find shortest path
# edit graph to avoid duplicate path
# repeat for k paths 
def k_shortest_path(graph, start, end, k=3):
    paths = []
    temp_graph = copy.deepcopy(graph)

    for _ in range(k):
        path, cost = dijkstra(temp_graph, start, end)

        if path is None:
            break

        paths.append((path, cost))

        if len(path) > 1:
            u = path[0]
            v = path[1]
            temp_graph[u] = [(n, w) for (n, w) in temp_graph[u] if n != v]

    return paths

