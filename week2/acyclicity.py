#Uses python3
import sys
sys.setrecursionlimit(2000)  # 필요한 경우 재귀 한도 조정

def acyclic(adj):
    n = len(adj)
    visited = [0] * n  # 모든 노드의 방문 상태를 0으로 초기화

    def dfs(v):
        visited[v] = 1  # 현재 노드를 현재 경로에 포함시킴
        for neighbor in adj[v]:
            if visited[neighbor] == 0:  # 이웃 노드를 아직 방문하지 않은 경우
                if dfs(neighbor):  # DFS 재귀 호출로 사이클 확인
                    return True
            elif visited[neighbor] == 1:  # 이웃 노드가 현재 경로에 있다면 사이클 존재
                return True
        visited[v] = 2  # 모든 이웃 노드 탐색 완료 후 방문 완료로 표시
        return False

    for v in range(n):
        if visited[v] == 0:  # 아직 방문하지 않은 노드에서 DFS 시작
            if dfs(v):  # 사이클이 발견되면 1 반환
                return 1
    return 0  # 사이클이 없는 경우 0 반환

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]  # 정점의 개수와 간선의 개수
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))  # 간선 리스트

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # 방향 간선 추가 (0 기반 인덱스로 조정)

    print(acyclic(adj))
