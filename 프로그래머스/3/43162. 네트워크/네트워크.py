def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for start in range(n):
        queue = [start]
        head = 0
        
        if visited[start]:
            continue
        answer += 1
        
        while head < len(queue):
            current = queue[head]
            head += 1
            
            for next_com in range(n):
                if not visited[next_com]:
                    if computers[current][next_com] == 1:
                        queue.append(next_com)
                        visited[next_com] = True
    
    return answer