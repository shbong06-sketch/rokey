# dfs.py

# 매개변수 : 그래프, 탐색 시작 노드
# 반환깂 : 방문한 리스트
myGraph = {
    "A" : ["B", "C", "D"],
    "B" : ["A", "E"],
    "C" : ["A", "F", "G"],
    "D" : ["A", 'H'],
    "E" : ["B", "I"],
    "F" : ["C", "J"],
    "G" : ["C"],
    "H" : ["D"],
    "I" : ["E"],
    "J" : ["F"]
}
# graph = myGraph
# start_node = 'A'
def my_dfs(graph, start_node):
    # 1. 탐색할 노드를 담을 스택(Stack) 자료형 생성
    stack = list()      # stack = []
    # 2. 방문 여부 확인 리스트 생성
    visited = list()    # visited = []        
    # 3. 탐색 시작 노드
    stack.append(start_node)    

    # 6. 더 이상 방문할 노드가 없을 때까지 4~5의 과정 반복
    # stack == []
    # len(stack) == 0
    while stack:
        # 4. 방문할 노드를 스택에서 제거
        node = stack.pop()
        # 5. 방문 리스트에 스택에서 꺼낸 노드가 없으면,
        if node not in visited:
            # 인접 노드를 스택에 추가
            # stack.append(graph[node])
            # stack.extend(graph[node])
            # ['B', 'C', 'D'] => ['D', 'C', 'B']
            stack.extend(reversed(graph[node]))     # 방문 순서를 순차적
            visited.append(node)        # 방문 처리
            print(f"visited: {visited}")
            print(f"stack: {stack}")
    return visited

print(my_dfs(myGraph, 'A'))
print("-----------------------")
from graph1 import myGraph1
print(my_dfs(myGraph1, 1))