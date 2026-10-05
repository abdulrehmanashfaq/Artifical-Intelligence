from collections import deque

class CppWalkthroughGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, v, w):
        self.adj[v].append(w)  # Directed edge v -> w

    def BFS(self, s):
        visited = [False] * self.V
        queue = deque()

        visited[s] = True
        queue.append(s)

        print(f"Following is Breadth First Traversal (starting from vertex {s}):")
        
        while queue:
            s = queue.popleft()
            print(s, end=" ")

            for neighbor in self.adj[s]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# Driver program matching C++ main()
if __name__ == "__main__":
    g = CppWalkthroughGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.BFS(2)