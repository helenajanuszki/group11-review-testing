import heapq

# distance starts at 0 and others with infinity
# min heap to keep track of cost by node
# pop the smallest node -> look at neighbors -> update distance 
# repeat
def dijkstra(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return path, cost
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return None, float('inf')