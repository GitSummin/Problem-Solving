def solution(progresses, speeds):
    answer = []
    days = []
    
    # 각 기능의 완료까지 걸리는 일수 계산
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress + speed - 1) // speed
        days.append(day)
    
    # 첫 번째 기능의 배포일
    deploy_day = days[0]
    count = 1
    
    # 두 번째 기능부터 확인
    for day in days[1:]:
        
        # 앞 기능의 배포일까지 이미 완료된다면 함께 배포
        if day <= deploy_day:
            count += 1
        
        # 앞 기능보다 늦게 끝난다면 새로운 배포 시작
        else:
            answer.append(count)
            deploy_day = day
            count = 1
    
    # 마지막 묶음 추가
    answer.append(count)
    
    return answer