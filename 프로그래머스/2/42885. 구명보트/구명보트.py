def solution(people, limit):
    answer = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit: # 가장 무거운 사람과 가장 가벼운 사람이 같이 탈 수 있으면
            left += 1 # 둘 다 태운다 -> left 이동
            right -= 1
        else:
            right -= 1 # 무거운 사람은 어쨌든 태운다 -> right 이동
        answer +=1 # 보트 한 대 사용
    
    return answer