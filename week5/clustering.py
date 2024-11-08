#Uses python3
import sys
import math

def clustering(x, y, k):
    # Create a list of all edges with distances between points
    edges = []
    n = len(x)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((dist, i, j))
    
    # Sort edges by distance
    edges.sort()
    
    # Union-Find data structure for Kruskal's algorithm
    parent = list(range(n))
    rank = [0] * n
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
    
    # Kruskal's algorithm to form clusters
    num_clusters = n
    for dist, u, v in edges:
        if find(u) != find(v):
            if num_clusters == k:
                # If we already have `k` clusters, this edge defines the spacing
                return dist
            union(u, v)
            num_clusters -= 1
    
    return -1.0  # In case we cannot form `k` clusters

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))