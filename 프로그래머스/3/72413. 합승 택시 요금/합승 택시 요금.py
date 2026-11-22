def solution(n, s, a, b, fares):    
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for u, v, fare in fares:
        dist[u][v] = dist[v][u] = fare
    
    for via in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
    
    return min(dist[s][k] + dist[k][a] + dist[k][b] for k in range(1, n+1))