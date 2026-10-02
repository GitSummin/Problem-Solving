def solution(numbers):
    # 기본값은 -1
    # 끝까지 더 큰 수를 못 찾은 원소는 그대로 -1이 남음
    answer = [-1] * len(numbers)

    # 아직 뒷 큰수를 찾지 못한 원소의 "인덱스"를 저장
    stack = []
    
    for i in range(len(numbers)):

        # 현재 숫자 numbers[i]가
        # stack 맨 위 인덱스의 숫자보다 크다면
        # 현재 숫자가 그 원소의 "가장 가까운 뒷 큰수"
        while stack and numbers[stack[-1]] < numbers[i]:

            # 뒷 큰수를 찾은 인덱스를 stack에서 제거
            idx = stack.pop()

            # 해당 위치의 정답을 현재 숫자로 저장
            answer[idx] = numbers[i]

        # 현재 숫자도 아직 자기보다 큰 뒷수가 없으므로
        # 인덱스를 stack에 저장
        stack.append(i)

    return answer