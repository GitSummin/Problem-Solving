def solution(n, times):
    left = 1 # 최소 시간 (1분)
    right = max(times) * n # 최대 시간 (가장 오래 걸리는 심시관 시간 * 대기 인원 수)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2 # 평균 시간
        people = 0
        
        for time in times:
            people += mid // time # 평균 시간 동안 몇 명을 처리할 수 있는지 계산
        
        if people >= n: # n명 이상 가능하면, 시간을 줄인다
            answer = mid
            right = mid -1
        else: # 그렇지 않으면, 시간을 늘린다
            left = mid + 1
            
    return answer