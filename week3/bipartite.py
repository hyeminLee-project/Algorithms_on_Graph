#Uses python3
import sys
import queue

def bipartite(adj):
    # Initialize colors array with -1 (unvisited)
    colors = [-1] * len(adj)
    
    # Go through each node in case the graph is disconnected
    for start in range(len(adj)):
        if colors[start] == -1:  # Not visited
            # Start BFS from this node
            q = queue.Queue()
            q.put(start)
            colors[start] = 0  # Assign initial color 0

            while not q.empty():
                u = q.get()
                
                for v in adj[u]:
                    if colors[v] == -1:
                        # Assign opposite color to the adjacent node
                        colors[v] = 1 - colors[u]
                        q.put(v)
                    elif colors[v] == colors[u]:
                        # If we find a node with the same color as its neighbor
                        return 0
    return 1

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
    print(bipartite(adj))