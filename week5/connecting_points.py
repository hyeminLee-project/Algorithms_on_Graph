#Uses python3
import sys
import math

def minimum_distance(x, y):
    # Create a list of all edges with their distances
    edges = []
    n = len(x)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((dist, i, j))
    
    # Sort edges by distance
    edges.sort()
    
    # Kruskal's algorithm with Union-Find
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
    
    # Calculate the total weight of the minimum spanning tree
    result = 0.0
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            result += dist
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))