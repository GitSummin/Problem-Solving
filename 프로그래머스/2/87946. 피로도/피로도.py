from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for order in permutations(dungeons):
        current_k = k
        count = 0
        
        for need, cost in order:
            if current_k >= need:
                current_k -= cost
                count += 1
            else:
                break
    
        answer = max(count, answer)
        
    return answer
