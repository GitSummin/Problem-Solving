def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        new_array = array[i-1:j]
        new_array.sort()
        
        answer.append(new_array[k-1])
            
    return answer