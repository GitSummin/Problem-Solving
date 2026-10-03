def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i, citation in enumerate(citations):
        h = i + 1

        # h번째 논문까지 모두 h번 이상 인용되었는지 확인
        if citation >= h:
            answer = h
        else:
            break

    return answer