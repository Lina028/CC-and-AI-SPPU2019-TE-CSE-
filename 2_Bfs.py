def bfs(visited, graph, start_node):
    queue = []
    visited.add(start_node)
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

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

    print("BFS Traversal:")
    bfs(visited, graph, 1)

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
# BFS Traversal:
# 1 2 3
# '''
#
# '''
# Same Graph Structure:
# 1 - 2
# |   |
# 3   4
# |
# 5
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
# 🔹 BFS Output:
# BFS Traversal:
# 1 2 3 4 5
# '''
