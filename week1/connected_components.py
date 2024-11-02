#Uses python3
import sys

def number_of_components(adj):
    def dfs(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor)

    n = len(adj)
    visited = [False] * n  # 모든 정점의 방문 여부를 저장하는 리스트
    result = 0  # 연결된 컴포넌트의 개수를 카운트

    for v in range(n):
        if not visited[v]:  # 아직 방문되지 않은 정점에서 DFS 시작
            dfs(v)
            result += 1  # 새로운 연결된 컴포넌트를 찾았으므로 결과 증가

    return result  # 총 연결된 컴포넌트 수 반환

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]  # 정점과 간선의 수
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)  # 무방향 간선 추가
        adj[b - 1].append(a - 1)

    print(number_of_components(adj))
