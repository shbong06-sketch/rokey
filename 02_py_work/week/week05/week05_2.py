# week05_2.py

data = {
    '두': ['산', '로', '키'],
    '산': ['두', '부'],
    '로': ['두'],
    '키': ['두', '트'],
    '부': ['산'],
    '트': ['키', '캠', '프'],
    '캠': ['트'],
    '프': ['트']
}

def my_dfs(graph, start_node):
    # 1. 빈 스택 생성
    stack = list()
    # 2. 방문 표시 리스트 생성
    visited = list()
    # 3. 시작 노드 삽입
    stack.append(start_node)
    # 6. 빈 스택이 될 때까지 반복
    while stack:
        # 4. 스택에서 노드 꺼내기
        node = stack.pop()
        # 5. 방문하지 않은 노드라면,
        if node not in visited:
            # 5-1. 방문처리
            visited.append(node)
            # 5-2. 인접 노드 스택에 추가
            stack.extend(reversed(graph[node]))
    return visited

print(my_dfs(data, '두'))

print("------------------------")
def my_bfs(graph, start_node):
    # 1. 빈 큐 생성
    queue = list()
    # 2. 방문 표시 리스트 생성
    visited = list()
    # 3. 시작 노드 삽입
    queue.append(start_node)
    # 6. 빈 큐가 될 때까지 반복
    while queue:
        # 4. 큐에서 노드 꺼내기
        node = queue.pop(0)
        # 5. 방문하지 않은 노드라면,
        if node not in visited:
            # 5-1. 방문처리
            visited.append(node)
            # 5-2. 인접 노드 큐에 추가
            queue.extend(graph[node])
    return visited

print(my_bfs(data, '두'))