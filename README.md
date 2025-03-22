# Python 그래프 탐색 알고리즘 예제

이 저장소는 파이썬으로 구현한 다양한 그래프 탐색 알고리즘의 예제를 포함하고 있습니다.

## 구현된 알고리즘

1. **BFS (너비 우선 탐색)**
   - 파일: `bfs_example.py`
   - 큐를 사용한 반복적 구현
   - 레벨 단위로 노드 탐색

2. **DFS (깊이 우선 탐색)**
   - 파일: `dfs_example.py`
   - 재귀를 사용한 구현
   - 한 경로를 끝까지 탐색 후 백트래킹

3. **Dijkstra (다익스트라 최단 경로)**
   - 파일: `dijkstra_example.py`
   - 우선순위 큐를 사용한 효율적인 구현
   - 가중치가 있는 그래프에서의 최단 경로 탐색
   - 최단 거리와 경로 모두 추적

## 사용 방법

1. 이 저장소를 클론합니다:
```bash
git clone https://github.com/Luna7997/python-bfs-example.git
```

2. Python이 설치되어 있는지 확인합니다.

3. 원하는 알고리즘 예제를 실행합니다:
```bash
python bfs_example.py    # BFS 실행
python dfs_example.py    # DFS 실행
python dijkstra_example.py  # Dijkstra 실행
```

4. 프롬프트가 표시되면 시작 노드를 입력합니다.

## 그래프 구조

### BFS와 DFS 예제
14개의 노드(A-N)로 구성된 무방향 그래프를 사용합니다.

### Dijkstra 예제
6개의 노드(A-F)로 구성된 가중치 그래프를 사용합니다:
```
A --- (4) --- B --- (5) --- D
|            /|            /|
|           / |           / |
(2)     (1)  |        (2)  |
|         /   |         /   |
|        /    |        /    |
C ----------------- E --- (3) --- F
     (10)          
```

## 요구사항

- Python 3.x
- collections 모듈 (기본 내장, BFS에서 사용)
- heapq 모듈 (기본 내장, Dijkstra에서 사용)

## 라이선스

MIT License