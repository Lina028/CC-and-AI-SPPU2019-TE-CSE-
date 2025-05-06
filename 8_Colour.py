class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list

    # Add an edge between two vertices
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Check if the current color assignment is valid
    def is_safe(self, v, color, c):
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True

    # Utility function to solve the graph coloring problem
    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True  # All vertices are assigned a color

        for c in range(1, m+1):  # Try different colors
            if self.is_safe(v, color, c):
                color[v] = c  # Assign color
                if self.graph_coloring_util(m, color, v + 1):  # Recur for next vertex
                    return True
                color[v] = 0  # Backtrack

        return False

    # Main function to solve the problem
    def graph_coloring(self, m):
        color = [0] * self.V  # Initialize color assignment for each vertex

        # Try to color the graph starting from the first vertex
        if not self.graph_coloring_util(m, color, 0):
            print("Solution does not exist")
            return False

        # Print the solution
        print("Solution exists: Coloring of vertices")
        for v in range(self.V):
            print(f"Vertex {v + 1} -> Color {color[v]}")
        return True

# Example 1: Complete Graph with 4 vertices
print("Example 1: Complete Graph with 4 vertices")
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(0, 3)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 3)
m1 = 4  # 4 colors needed
g1.graph_coloring(m1)
print()

# Example 2: Linear Chain with 5 vertices
print("Example 2: Linear Chain with 5 vertices")
g2 = Graph(5)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
m2 = 2  # 2 colors needed
g2.graph_coloring(m2)
print()

# Example 3: Tree Structure with 6 vertices (bipartite graph)
print("Example 3: Tree Structure with 6 vertices")
g3 = Graph(6)
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(2, 5)
m3 = 2  # 2 colors needed (tree is bipartite)
g3.graph_coloring(m3)
print()

# Example 4: Cycle Graph with 5 vertices (odd cycle)
print("Example 4: Cycle Graph with 5 vertices (odd cycle)")
g4 = Graph(5)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(2, 3)
g4.add_edge(3, 4)
g4.add_edge(4, 0)
m4 = 3  # 3 colors needed for odd cycle
g4.graph_coloring(m4)
print()

# Example 5: Disconnected Graph with 7 vertices
print("Example 5: Disconnected Graph with 7 vertices")
g5 = Graph(7)
g5.add_edge(0, 1)
g5.add_edge(0, 2)
g5.add_edge(3, 4)
g5.add_edge(4, 5)
g5.add_edge(5, 6)
m5 = 2  # 2 colors needed for disconnected graph
g5.graph_coloring(m5)
print()

# Example 6: Star-shaped Graph with 6 vertices
print("Example 6: Star-shaped Graph with 6 vertices")
g6 = Graph(6)
g6.add_edge(0, 1)
g6.add_edge(0, 2)
g6.add_edge(0, 3)
g6.add_edge(0, 4)
g6.add_edge(0, 5)
m6 = 2  # 2 colors needed for star-shaped graph
g6.graph_coloring(m6)
print()
