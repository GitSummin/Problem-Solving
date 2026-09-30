def solution(N, stages):
    failure = {}
    
    # 현재 해당 스테이지 이상까지 도달한 사람 수
    remain = len(stages)
    
    for stage in range(1, N + 1):
        # 현재 스테이지에서 멈춘 사람 수
        fail_count = stages.count(stage)
        
        # 도달한 사람이 없는 경우
        if remain == 0:
            failure[stage] = 0
        else:
            failure[stage] = fail_count / remain
        
        # 현재 스테이지에서 멈춘 사람은
        # 다음 스테이지에는 도달하지 못했으므로 제외
        remain -= fail_count
    
    # 실패율 내림차순
    # 실패율이 같으면 stage 번호 오름차순
    answer = sorted(
        failure,
        key=lambda x: (-failure[x], x)
    )
    
    return answer