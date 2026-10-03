def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, k = command
        
        cut_array = array[start-1:end]
        cut_array.sort()
        answer.append(cut_array[k-1])
    
    return answer