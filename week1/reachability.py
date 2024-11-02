#Uses python3

import sys
sys.setrecursionlimit(2000)  # 필요한 경우 재귀 한도를 늘려 깊은 탐색을 지원

def reach(adj, x, y):
    visited = [False] * len(adj)  # 각 정점의 방문 여부를 저장하는 리스트

    def dfs(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(x)  # 정점 x에서 DFS 시작
    return 1 if visited[y] else 0  # y가 방문되었는지 여부로 결과 반환

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1  # 0 기반 인덱스로 조정
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # 무방향 간선 추가
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
