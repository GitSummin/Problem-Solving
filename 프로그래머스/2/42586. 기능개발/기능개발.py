import math

def solution(progresses, speeds):
    answer = []
    time_lst = []
    
    for i in range(len(progresses)):
        time = float((100 - progresses[i]) / speeds[i])
        time = math.ceil(time)
        time_lst.append(time)
    
    deploy_day = time_lst[0]
    count = 1
    
    for i in range(1, len(time_lst)):
        if time_lst[i] <= deploy_day:
            count += 1
        else:
            answer.append(count)
            deploy_day = time_lst[i]
            count = 1
            
    answer.append(count)
    
    return answer