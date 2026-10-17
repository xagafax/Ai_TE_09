from collections import deque

class NetworkSearch:
    """Mencari rute/jalur cadangan terpendek di jaringan menggunakan Breadth-First Search (BFS)"""
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(self, start, goal):
        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None