def solution(players, m, k):
    answer = 0

    expire = [0] * (len(players) + k) # 시간별 운영이 종료되는 서버 수
    active = 0 # 현재 운영 중인 증설 서버 수

    for i, play_num in enumerate(players):
        active -= expire[i] # 운영 시간이 끝난 서버 반납
        required = play_num // m # 현재 시간에 필요한 증설 서버 수

        # 서버가 부족하다면 추가 증설
        if required > active:
            add = required - active

            active += add
            answer += add

            # k시간 이후 서버 반납 예정
            expire[i + k] += add

    return answer