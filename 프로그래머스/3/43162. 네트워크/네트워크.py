def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
        answer += 1

        queue = [start]
        head = 0
        visited[start] = True

        while head < len(queue):
            current = queue[head]
            head += 1

            for next_com in range(n):
                if computers[current][next_com] == 1:
                    if not visited[next_com]:
                        visited[next_com] = True
                        queue.append(next_com)
    
    return answer