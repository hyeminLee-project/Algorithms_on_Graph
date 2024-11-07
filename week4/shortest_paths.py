# Uses python3
import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    
    # 시작 노드의 거리를 0으로 초기화하고 도달 가능으로 표시
    distance[s] = 0
    reachable[s] = 1

    # 벨만-포드 알고리즘을 통해 최단 거리 계산 (최대 n-1번 반복)
    for _ in range(n - 1):
        updated = False
        for u in range(n):
            if distance[u] == float('inf'):
                continue
            for idx, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][idx]:
                    distance[v] = distance[u] + cost[u][idx]
                    reachable[v] = 1
                    updated = True
        if not updated:
            break

    # 음의 사이클이 있는지 확인하기 위해 한 번 더 갱신 시도
    for _ in range(n):
        for u in range(n):
            if distance[u] == float('inf'):
                continue
            for idx, v in enumerate(adj[u]):
                # 음의 사이클이 발생하면 해당 노드를 shortest에서 제외
                if distance[v] > distance[u] + cost[u][idx]:
                    distance[v] = distance[u] + cost[u][idx]
                    reachable[v] = 1
                    shortest[v] = 0  # 음의 사이클에 영향 받는 노드로 표시

    # 음의 사이클에 연결된 모든 노드들도 shortest에서 제외
    q = queue.Queue()
    for u in range(n):
        if shortest[u] == 0:
            q.put(u)

    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if shortest[v] == 1:
                shortest[v] = 0
                q.put(v)

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
    
    s = data[0] - 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
