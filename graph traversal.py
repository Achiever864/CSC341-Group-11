# DFS Traversal
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node)
        visited.append(node)

        for neighbor in graph[node]:
            dfs(neighbor)

dfs('A')

#BFS Traversal
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

visited = []
queue = []

def bfs(node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs('A')