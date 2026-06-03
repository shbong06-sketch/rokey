# hw17_1.py

# 6.
graph = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]
# 7.
for line in graph:
    print(line)

# 8.
# row = int(input("세로 길이를 입력하세요:"))
# column = int(input("가로 길이를 입력하세요:"))
# graph = list()
# for i in range(row):
#     graph.append(list(map(int, input().split())))

# for line in graph:
#     print(line)

# 9.
# 지도 탐색 -> 0: 길/ 1: 벽

def dfs_solve_maze(graph, start):
    stack = list()      # 1. 탐색할 노드를 저장할 스택 생성
    visited = list()    # 2. 지나간 길 저장할 리스트 생성
    stack.append(start) # 3. 스택에 시작 지점(0,0) 삽입
    
    while stack:    # 6. 더이상 탐색할 노드가 없을 때까지 반복
        r, c = stack.pop()          # 4. 탐색할 노드(raw, column) 스택에서 꺼내기
        if (r, c) not in visited:   # 5. 지나간 길이 아니면,
            visited.append((r, c))  # 5-1. 방문 처리

            # 5-2. 상, 하, 좌, 우 연결된 노드의 값이 0이면, + 탐색할 노드가 범위(0~6미만) 내이면
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(graph[0]) and 0 <= nc < len(graph) and graph[nr][nc] == 0:
                    # 5-2-a. 다음 탐색할 노드를 스택에 삽입
                    stack.append((nr, nc))
    return visited

print(f"로봇 탐색 경로: {dfs_solve_maze(graph, (0,0))}")

def bfs_solve_maze(graph, start):
    queue = list()      # 1. 탐색할 노드를 저장할 큐 생성
    visited = list()    # 2. 지나간 길을 저장할 리스트 생성
    queue.append(start) # 3. 큐에 시작 지점 삽입

    while queue:        # 6. 더이상 탐색할 노드가 없을 때까지 반복
        r, c = queue.pop(0)         # 4. 탐색할 노드 큐에서 꺼내기
        if (r, c) not in visited:   # 5. 지나간 길이 아니라면
            visited.append((r, c))  # 5-1. 방문 처리

            # 5-2. 상, 하, 좌, 우에 연결된 노드의 값이 0이고, 범위가 그래프 내라면,
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(graph[0]) and 0 <= nc < len(graph) and graph[nr][nc] == 0:
                    # 5-2-a. 다음 탐색할 노드를 큐에 삽입
                    queue.append((nr, nc))
    return visited

print(f"로봇 탐색 경로: {bfs_solve_maze(graph, (0,0))}")