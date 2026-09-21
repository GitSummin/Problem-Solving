def solution(numbers, target):
    
#     # (1) DFS 풀이
#     def dfs(index, current_sum):
#         if index == len(numbers):
#             if current_sum == target:
#                 return 1
#             return 0
    
#         plus = dfs(index + 1, current_sum + numbers[index])
#         minus = dfs(index + 1, current_sum - numbers[index])
        
#         return plus + minus
    
#     return dfs(0, 0)


    # (2) BFS 풀이
    answer = 0
    
    queue = [(0,0)]
    head = 0

    while head < len(queue):
        index, current_sum = queue[head]
        head += 1
        
        if index == len(numbers):
            if target == current_sum:
                answer += 1
            continue
            
        queue.append((index+1, current_sum + numbers[index]))
        queue.append((index+1, current_sum - numbers[index]))
        
    return answer
        
        
        