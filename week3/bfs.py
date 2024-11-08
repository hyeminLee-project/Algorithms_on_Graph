#Uses python3

import sys
import queue

def distance(adj, s, t):
    # If the start and target nodes are the same
    if s == t:
        return 0

    # Initialize the distance array with -1 (unvisited nodes)
    distances = [-1] * len(adj)
    distances[s] = 0  # Starting node distance is 0

    # Queue for BFS
    q = queue.Queue()
    q.put(s)

    # BFS loop
    while not q.empty():
        current = q.get()

        # Explore each neighbor
        for neighbor in adj[current]:
            if distances[neighbor] == -1:  # If unvisited
                distances[neighbor] = distances[current] + 1
                q.put(neighbor)
                
                # If we reached the target node
                if neighbor == t:
                    return distances[neighbor]

    # Return -1 if there is no path from s to t
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
설명