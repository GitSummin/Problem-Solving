def solution(distance, rocks, n):
    rocks = sorted(rocks)
    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        removed = 0
        last = 0

        for rock in rocks:
            if rock - last < mid:
                removed += 1
            else:
                last = rock

        if distance - last < mid:
            removed += 1

        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer