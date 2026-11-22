def solution(play_time, adv_time, logs):
    def to_seconds(time):
        h, m, s = map(int, time.split(":"))
        return h * 3600 + m * 60 + s

    play = to_seconds(play_time)
    adv = to_seconds(adv_time)
    diff = [0] * (play + 1)

    for log in logs:
        start, end = map(to_seconds, log.split("-"))
        diff[start] += 1
        diff[end] -= 1

    prefix = [0] * (play + 1)
    viewers = 0
    for t in range(play):
        viewers += diff[t]                  # t초에 시청 중인 인원
        prefix[t + 1] = prefix[t] + viewers

    best_start = 0
    best_watch_time = prefix[adv]

    for start in range(1, play - adv + 1):
        watch_time = prefix[start + adv] - prefix[start]
        if watch_time > best_watch_time:
            best_watch_time = watch_time
            best_start = start

    hours, remaining = divmod(best_start, 3600)
    minutes, seconds = divmod(remaining, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"