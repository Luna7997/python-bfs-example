from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 예제 그래프 (인접 리스트로 표현)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G', 'H'],
    'D': ['A', 'I'],
    'E': ['B', 'J'],
    'F': ['B', 'K'],
    'G': ['C', 'L'],
    'H': ['C', 'M'],
    'I': ['D', 'N'],
    'J': ['E', 'K'],
    'K': ['F', 'J'],
    'L': ['G', 'M'],
    'M': ['H', 'L'],
    'N': ['I']
}

start_node = input("시작 노드를 입력하세요 (A-N): ")
print(f"BFS 탐색 결과 (시작 노드: {start_node}):")
bfs(graph, start_node)