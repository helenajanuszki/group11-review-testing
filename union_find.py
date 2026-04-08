class UnionFind:
    # nodes are all the nodes in a graph
    def __init__(self, nodes):
        # Cities and their root/parent city {city: root}, cities are their own roots to start
        self.parent_cities = {i: i for i in nodes}

    def find(self, x: int) -> int:
        """Recursively searches for the root of a node

        Args:
            x (int): node whose root is being searched for

        Returns:
            Root node of x as an integer
        """

        if x == self.parent_cities[x]:
            return x

        return self.find(self.parent_cities[x])

    def union(self, source: int, destination: int) -> bool:
        """Checks if the destination's root is the source's root (a cycle), 
        points the source root to destination root otherwise

        Args:
            source (int): source of a ticket
            destination (int): destination of a ticket

        Returns:
            True if union was a success, False if a cycle was found
        """

        source_root = self.find(source)
        destination_root = self.find(destination)

        if source_root == destination_root:
            return False

        self.parent_cities[source_root] = destination_root
        return True

    def snapshot(self) -> dict:
        """
        Returns a copy of the current parent dict
        """

        return self.parent_cities.copy()

    def restore_snapshot(self, snapshot: dict):
        """Restores parent dict to a previous state

        Args:
            snapshot (dict): a previous state of parent_cities from snapshot()
        """

        if not isinstance(snapshot, dict):
            raise TypeError(f"parent_cities is a dict, not a {type(snapshot)}")

        self.parent_cities = snapshot

    def detect_cycle(self, paths: list) -> list:
        """Finds the first valid path from a list of candidate paths that does not have a cycle.

        Args:
            paths (list): list of (path, cost) tuples from k_shortest_path

        Returns:
            A list containing the chosen (path, cost) tuple, or empty list if all paths form cycles
        """
        chosen_path = None
        for path, cost in paths:
            snap = self.snapshot()
            cycle_found = False

            for i in range(len(path) - 1):
                if not self.union(path[i], path[i + 1]):
                    cycle_found = True
                    break

            if cycle_found:
                self.restore_snapshot(snap)
            else:
                chosen_path = (path, cost)
                break

        return [chosen_path] if chosen_path else []
    