def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])    
    last_end = -1
    
    for start, end in targets:
        if start >= last_end:
            answer += 1
            last_end = end
    
    return answer