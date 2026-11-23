from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    
    for a, b, time in paths:
        graph[a].append((b, time))
        graph[b].append((a, time))
    
    dist = [float("inf")] * (n+1)
    heap = []
    
    for gate in gates:        
        dist[gate] = 0
        heappush(heap, (0, gate))
        
    while heap:
        current_intensity, now = heappop(heap)
        if current_intensity > dist[now]:
            continue
        
        if now in summits:
            continue
            
        for next_node, time in graph[now]:
            candidate = max(current_intensity, time)
            
            if candidate < dist[next_node]:
                dist[next_node] = candidate
                heappush(heap, (candidate, next_node))
    
    best_summit = min(summits, key=lambda s: (dist[s], s))
    return [best_summit, dist[best_summit]]