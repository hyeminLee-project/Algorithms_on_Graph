#Uses python3

import sys
sys.setrecursionlimit(200000)  # 재귀 한도 설정

def dfs(adj, used, order, x):
    """
    정점 x에서 DFS를 수행하여 위상 정렬 순서를 찾음.
    - adj: 인접 리스트
    - used: 방문 여부를 기록하는 리스트
    - order: 방문 완료 순서를 기록할 리스트
    - x: 현재 탐색 중인 정점
    """
    used[x] = 1  # 현재 정점을 방문 처리
    for neighbor in adj[x]:
        if not used[neighbor]:  # 방문하지 않은 인접 정점에 대해 DFS 수행
            dfs(adj, used, order, neighbor)
    order.append(x)  # 모든 인접 정점을 탐색한 후 현재 정점을 결과에 추가

def toposort(adj):
    """
    DAG의 위상 정렬을 수행하여 정점의 순서를 반환.
    - adj: 인접 리스트
    """
    used = [0] * len(adj)  # 모든 정점의 방문 여부를 0으로 초기화
    order = []  # 방문 완료 순서를 저장할 리스트

    # 모든 정점에 대해 DFS 수행
    for v in range(len(adj)):
        if not used[v]:  # 방문하지 않은 정점에서 DFS 시작
            dfs(adj, used, order, v)

    order.reverse()  # DFS 완료 후 역순으로 정렬
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]  # 정점과 간선의 개수
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))  # 간선 정보 추출
    
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # 방향 간선 추가 (0 기반 인덱스 사용)

    order = toposort(adj)  # 위상 정렬 수행
    for x in order:
        print(x + 1, end=' ')  # 0 기반 인덱스를 다시 1 기반으로 출력
