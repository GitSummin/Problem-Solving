def solution(arr):
    answer = []
    
    for value in arr:
        if len(answer) == 0:
            answer.append(value)
        if value != answer[-1]:
            answer.append(value)
        
    return answer