def solution(n, wires):
    answer = n
    
    for cut in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        
        for i, (a, b) in enumerate(wires):
            if i == cut:
                continue            
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n+1)
        queue = [1]
        head = 0
        visited[1] = True
        count = 1
        
        while head < len(queue):
            current = queue[head]
            head += 1
            
            for next_node in graph[current]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1
        
        difference = abs(count - (n-count))
        answer = min(answer, difference)
    
    return answer