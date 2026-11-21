def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        cut_arr = sorted(array[i-1: j])
        answer.append(cut_arr[k-1])
    
    return answer