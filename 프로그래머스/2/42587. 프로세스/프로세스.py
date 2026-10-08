from collections import deque

def solution(priorities, location):
    queue = deque()
    
    for i, priority in enumerate(priorities):
        queue.append((priority, i))
    count = 0
    
    while queue:
        priority, index = queue.popleft()
        
        if any(priority < other_priority for other_priority, _ in queue):
            queue.append((priority, index))
        else:
            count += 1
            
            if index == location:
                return count
        
    return 