from collections import deque

class Graph:
    def __init__(self):
        # Adjacency list representation
        self.adj = {}

    def add_edge(self, u, v, directed=False):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)

            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal

# Driver Code for Task 1 (Section 4.1 Graph)
if __name__ == "__main__":
    g = Graph()
    
    # Adding edges based on graph in Section 4.1
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("BFS Traversal starting from node 0:")
    result = g.bfs(0)
    print(" -> ".join(map(str, result)))