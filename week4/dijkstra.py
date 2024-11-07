# Uses python3
import sys
import heapq

def distance(adj, cost, s, t):
    # 노드 수만큼 무한대 값으로 거리 배열 초기화
    n = len(adj)
    distances = [float('inf')] * n
    distances[s] = 0  # 시작 노드의 거리는 0으로 설정

    # 우선순위 큐 초기화: (거리, 노드) 형태
    pq = [(0, s)]
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        # 현재 노드까지의 거리가 기록된 최소 거리보다 크면 무시
        if current_distance > distances[u]:
            continue

        # 인접 노드를 확인하고, 거리 갱신이 가능하면 큐에 삽입
        for i, v in enumerate(adj[u]):
            weight = cost[u][i]
            distance = current_distance + weight

            if distance < distances[v]:  # 최단 경로 갱신
                distances[v] = distance
                heapq.heappush(pq, (distance, v))

    # 도착 노드까지의 최소 거리를 반환, 경로가 없으면 -1 반환
    return distances[t] if distances[t] != float('inf') else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    
    # 입력 파싱
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    
    # 인접 리스트와 비용 리스트 생성
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
