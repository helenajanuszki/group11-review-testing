import numpy as np
from collections import defaultdict

matrix = np.array([[0,0,0,8,4,0,0,0],
                  [2,0,0,0,0,0,11,0],
                  [0,0,0,0,0,11,1,0],
                  [0,6,0,0,0,0,0,9],
                  [0,0,0,0,0,0,5,0],
                  [0,0,0,0,0,0,2,2],
                  [0,0,4,0,5,0,0,0],
                  [0,0,0,0,0,3,0,0],
                  ])


def main():
    g = build_graph(matrix)
    tickets = [(1,6),(6,2),(2,5),(5,7)]

def build_graph(adj_matrix):
    graph = defaultdict(list)
    n = len(adj_matrix)

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0:  # edge exists
                graph[i].append((j, adj_matrix[i][j]))

    return graph