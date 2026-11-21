def solution(sequence, k):
    total = 0
    left = 0
    best = []
    best_len = float("inf")

    for right, value in enumerate(sequence):
        total += value

        while total > k:
            total -= sequence[left]
            left += 1

        if total == k:
            length = right - left + 1
            if length < best_len:
                best_len = length
                best = [left, right]

    return best