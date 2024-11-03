#Uses python3

import sys
sys.setrecursionlimit(200000)  # 재귀 한도 설정

def dfs(v, adj, visited, stack=None):
    """
    DFS를 수행하여 방문한 순서를 스택에 추가하거나 강한 연결 요소를 찾음
    - v: 현재 정점
    - adj: 그래프의 인접 리스트
    - visited: 방문 여부를 기록하는 리스트
    - stack: 방문 완료 순서대로 정점을 추가할 스택 (첫 번째 DFS에서 사용)
    """
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, stack)
    if stack is not None:
        stack.append(v)  # 첫 번째 DFS의 경우 스택에 정점을 추가

def number_of_strongly_connected_components(adj):
    n = len(adj)
    visited = [False] * n
    stack = []

    # 1. 첫 번째 DFS: 그래프에서 각 정점을 탐색하여 스택에 추가
    for v in range(n):
        if not visited[v]:
            dfs(v, adj, visited, stack)

    # 2. 전치 그래프 생성: 모든 간선 방향을 반대로 설정
    transpose_adj = [[] for _ in range(n)]
    for v in range(n):
        for neighbor in adj[v]:
            transpose_adj[neighbor].append(v)

    # 3. 두 번째 DFS: 스택에서 정점을 하나씩 꺼내며 전치 그래프 탐색
    visited = [False] * n
    scc_count = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs(v, transpose_adj, visited)  # 전치 그래프에서 DFS 수행
            scc_count += 1  # 하나의 강한 연결 요소를 찾음

    return scc_count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]  # 정점과 간선의 수
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # 방향 간선 추가 (0 기반 인덱스 사용)

    print(number_of_strongly_connected_components(adj))
