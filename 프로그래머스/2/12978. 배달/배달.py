def solution(N, road, K):
    inf = float("inf")
    dist = [inf] * N
    dist[0] = 0
    
    visited = [False] * N
    graph = [[] for _ in range(N)]
    
    for a, b, time in road:
        graph[a-1].append((b-1, time))
        graph[b-1].append((a-1, time))
            
    for _ in range(N):
        u = -1
        min_time = inf
        
        for i in range(N):
            if not visited[i] and dist[i] < min_time:
                u = i
                min_time = dist[i]
        if u == -1:
            break
        visited[u] = True
                
        for v, time in graph[u]:
            candidate = dist[u] + time
            if candidate < dist[v]:
                dist[v] = candidate
        
    return sum(time <= K for time in dist)