# bfs.py
'''
BFS(Breath-First-Search)
'''
from graph import myGraph

def my_bfs(graph, start_node):
    # 1. 방문(탐색)할 노드를 담을 큐
    queue = list()
    # 2. 방문한 노드를 담을 리스트
    visited = list()
    # 3. 탐색 시작 노드를 큐에 삽입
    queue.append(start_node)

    # 6. 더 이상 방문할 노드가 없을 때까지 4~5의 과정 반복
    while queue:
        # 4. 큐에서 노드를 꺼냄.
        node = queue.pop(0)
        # 5. 방문하지 않았다면, 
        if node not in visited:
            # 인접 노드를 큐에 삽입
            queue.extend(graph[node])
            # 방문 처리
            visited.append(node)
            # print(f"visited : {visited}")
            # print(f"queue : {queue}")
    return visited

print(my_bfs(myGraph, 'A'))
print(my_bfs(myGraph, 'I'))
print(my_bfs(myGraph, 'C'))