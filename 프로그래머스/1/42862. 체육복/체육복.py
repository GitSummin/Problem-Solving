def solution(n, lost, reserve):
    # 도난 + 여벌이 동시에 있는 학생 제거
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)

    for person in sorted(real_reserve):
        # 앞번호 학생에게 먼저 빌려주기
        if person - 1 in real_lost:
            real_lost.remove(person - 1)

        # 앞번호가 필요 없으면 뒷번호에게
        elif person + 1 in real_lost:
            real_lost.remove(person + 1)

    return n - len(real_lost)