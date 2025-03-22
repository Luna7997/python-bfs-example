def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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
print(f"DFS 탐색 결과 (시작 노드: {start_node}):")
dfs(graph, start_node)