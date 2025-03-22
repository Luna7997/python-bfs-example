import heapq

def dijkstra(graph, start):
    # 거리 저장 딕셔너리 초기화
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # 우선순위 큐 초기화
    priority_queue = [(0, start)]
    # 경로 저장을 위한 딕셔너리
    path = {start: [start]}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 현재 거리가 이미 저장된 거리보다 크면 스킵
        if current_distance > distances[current_node]:
            continue
            
        # 인접 노드들을 확인
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로를 찾은 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 경로 업데이트
                path[neighbor] = path[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, path

# 예제 그래프 (인접 리스트로 표현, 가중치 포함)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

# 시작 노드 입력 받기
start_node = input("시작 노드를 입력하세요 (A-F): ")
print(f"\nDijkstra 알고리즘 결과 (시작 노드: {start_node})")

# 알고리즘 실행
distances, paths = dijkstra(graph, start_node)

# 결과 출력
print("\n각 노드까지의 최단 거리:")
for node in sorted(distances.keys()):
    print(f"{node}: {distances[node]}")

print("\n각 노드까지의 최단 경로:")
for node in sorted(paths.keys()):
    if node != start_node:
        path_str = ' -> '.join(paths[node])
        print(f"{node}: {path_str} (거리: {distances[node]})")