# Uses python3
import sys

def negative_cycle(adj, cost):
    n = len(adj)
    
    # 가상의 시작 노드를 추가
    distances = [float('inf')] * (n + 1)
    distances[n] = 0  # 가상의 노드 거리 초기화
    
    # 모든 노드로 향하는 0 가중치 간선을 추가
    adj.append([i for i in range(n)])
    cost.append([0] * n)

    # 벨만-포드 알고리즘 적용
    for i in range(n):
        updated = False
        for u in range(n + 1):
            for idx, v in enumerate(adj[u]):
                if distances[u] != float('inf') and distances[v] > distances[u] + cost[u][idx]:
                    distances[v] = distances[u] + cost[u][idx]
                    updated = True
                    if i == n - 1:
                        return 1  # 음의 사이클 존재
        if not updated:
            break  # 더 이상 갱신이 없으면 반복 종료
    
    return 0  # 음의 사이클이 존재하지 않음

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    
    # 그래프를 인접 리스트로 변환
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    
    # 음의 사이클 검사
    print(negative_cycle(adj, cost))
