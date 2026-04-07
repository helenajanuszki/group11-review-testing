from graph import build_graph
from k_shortest import k_shortest_path
from path_utils import format_path

def main():
    # randomly chosen edges
    edges = [
        (0, 1, 8),
        (0, 4, 4),
        (1, 3, 6),
        (1, 6, 2),
        (1, 5, 11),
        (2, 6, 1),
        (3, 5, 9),
        (4, 6, 5),
        (5, 7, 3),
        (6, 2, 4),
        (6, 7, 2)
    ]

    graph = build_graph(edges)

    tickets = [
        (0, 6),
        (1, 7)
    ]

    for ticket in tickets:
        paths = k_shortest_path(graph, ticket[0], ticket[1], k=3)
        result = format_path(ticket, paths)
        print("\nTicket:", ticket)
        for p in result["paths"]:
            print("Path:", p["path"], "Cost:", p["cost"])

if __name__ == "__main__":
    main()