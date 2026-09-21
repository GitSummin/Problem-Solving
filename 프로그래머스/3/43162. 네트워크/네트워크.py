def solution(n, computers):

    # (1) DFS
#     answer = 0
#     visited = [False] * n
    
#     def dfs(current):
#         visited[current] = True
        
#         for next_com in range(n):
#             if computers[current][next_com] == 1:
#                 if not visited[next_com]:
#                     dfs(next_com)
    
#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             answer += 1

#     return answer

    # (2) BFS
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
                    