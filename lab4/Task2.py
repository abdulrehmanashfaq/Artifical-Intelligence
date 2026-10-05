from collections import deque

class Graph:
    def __init__(self):
        # Adjacency list storing node connections
        self.adj = {}

    def add_edge(self, u, v, directed=True):
        """Adds an edge from node u to node v."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
            
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)

    def bfs(self, start_node):
        """Performs a full Breadth-First Search traversal of all reachable nodes."""
        if start_node not in self.adj:
            return []

        visited = {start_node}
        queue = deque([start_node])
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)

            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal

    def bfs_search_goal(self, start_node, goal_node):
        """Performs BFS and stops immediately when the goal node is expanded."""
        if start_node not in self.adj:
            return []

        visited = {start_node}
        queue = deque([start_node])
        expanded_nodes = []

        while queue:
            current_node = queue.popleft()
            expanded_nodes.append(current_node)

            # Stop search as soon as goal is reached
            if current_node == goal_node:
                return expanded_nodes

            for neighbor in self.adj.get(current_node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return expanded_nodes


if __name__ == "__main__":
    g = Graph()

    # Tree data definition
    tree_edges = {
        'A': ['B', 'F', 'D', 'E'],
        'B': ['K', 'J'],
        'F': [],
        'D': ['G'],
        'E': ['C', 'H', 'I'],
        'K': ['N', 'M'],
        'J': [],
        'G': [],
        'C': [],
        'H': [],
        'I': ['L'],
        'N': [],
        'M': [],
        'L': []
    }

    # Populate graph using add_edge
    for parent, children in tree_edges.items():
        for child in children:
            g.add_edge(parent, child, directed=True)

    start_node = 'A'
    goal_node = 'G'

    # 1. Full BFS Traversal
    full_traversal = g.bfs(start_node)
    print("Full BFS Traversal:")
    print(" -> ".join(full_traversal))

    print("\n" + "-" * 40 + "\n")

    # 2. BFS Goal Search
    goal_expanded = g.bfs_search_goal(start_node, goal_node)
    print(f"BFS Expansion Order to reach Goal '{goal_node}':")
    print(" -> ".join(goal_expanded))