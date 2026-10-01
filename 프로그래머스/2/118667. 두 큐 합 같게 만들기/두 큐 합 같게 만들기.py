from collections import deque

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    total = sum1 + sum2

    if total % 2 != 0:
        return -1
    
    target = total // 2
    count = 0
    
    max_count = len(queue1) * 4
    
    while count < max_count:
        
        if sum1 == target:
            return count
        
        elif sum1 > target:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
            
        else:
            value = q2.popleft()
            q1.append(value)
            sum2 -= value
            sum1 += value
            
        count += 1
    
    return -1