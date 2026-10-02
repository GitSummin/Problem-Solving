from collections import deque

def solution(queue1, queue2):
    
    # 맨 앞 원소를 빠르게 꺼내기 위해 deque로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 각 큐의 현재 합
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # 두 큐 전체 원소의 총합
    total = sum1 + sum2

    # 전체 합이 홀수라면 두 큐의 합을 똑같이 만들 수 없음
    if total % 2 != 0:
        return -1
    
    # 각 큐가 만들어야 하는 목표 합
    target = total // 2
    
    # 원소를 옮긴 횟수
    count = 0
    
    # 불가능한 경우 무한 반복되는 것을 막기 위한 최대 시도 횟수
    max_count = len(queue1) * 4
    
    while count < max_count:
        
        # q1의 합이 목표값이 되면
        # 전체 합이 고정되어 있으므로 q2도 자동으로 target이 됨
        if sum1 == target:
            return count
        
        # q1의 합이 너무 크면
        # q1의 맨 앞 원소를 q2로 이동
        elif sum1 > target:
            value = q1.popleft()
            q2.append(value)
            
            # 이동한 원소만큼 두 큐의 합 갱신
            sum1 -= value
            sum2 += value
            
        # q1의 합이 목표보다 작으면
        # q2의 맨 앞 원소를 q1으로 이동
        else:
            value = q2.popleft()
            q1.append(value)
            
            # 이동한 원소만큼 두 큐의 합 갱신
            sum2 -= value
            sum1 += value
            
        # 원소 하나를 옮겼으므로 작업 횟수 +1
        count += 1
    
    # 최대 횟수까지 시도했는데도 같아지지 않으면 불가능
    return -1