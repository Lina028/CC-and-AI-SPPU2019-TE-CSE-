def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def main():
    visited = set()
    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(edges):
            node = int(input(f"Enter edge {j+1} for node {i}: "))
            graph[i].append(node)

    print("DFS Traversal:")
    dfs(visited, graph, 1)

if __name__ == "__main__":
    main()

# '''
# 🔹 Example Input:
# Enter number of nodes: 3
# Enter number of edges for node 1: 2
# Enter edge 1 for node 1: 2
# Enter edge 2 for node 1: 3
# Enter number of edges for node 2: 0
# Enter number of edges for node 3: 0
#
# 🔹 Output:
# DFS Traversal:
# 1 2 3
# '''
#
# '''
# Graph Structure:
# 1 - 2
# |   |
# 3   4
# |
# 5
#
# This means:
# - Node 1 connects to 2 and 3
# - Node 2 connects to 4
# - Node 3 connects to 5
#
# 🔹 Input:
# Enter number of nodes: 5
# Enter number of edges for node 1: 2
# Enter edge 1 for node 1: 2
# Enter edge 2 for node 1: 3
# Enter number of edges for node 2: 1
# Enter edge 1 for node 2: 4
# Enter number of edges for node 3: 1
# Enter edge 1 for node 3: 5
# Enter number of edges for node 4: 0
# Enter number of edges for node 5: 0
#
# 🔹 DFS Output:
# DFS Traversal:
# 1 2 4 3 5
#'''