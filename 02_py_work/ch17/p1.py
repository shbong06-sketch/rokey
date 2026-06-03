# p1.py
# p.20

from graph1 import myGraph1

def my_bfs(graph, start_node):
    queue = list()
    visited = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    return visited

print(my_bfs(myGraph1, 6))