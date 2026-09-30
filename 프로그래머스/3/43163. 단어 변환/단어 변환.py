def solution(begin, target, words):
    # target 자체가 words에 없으면 변환 불가능
    if target not in words:
        return 0

    visited = [False] * len(words)

    # (현재 단어, 변환 횟수)
    queue = [(begin, 0)]
    head = 0

    while head < len(queue):
        current, count = queue[head]
        head += 1

        # target에 도착
        if current == target:
            return count

        for i, word in enumerate(words):
            if visited[i]:
                continue

            # 현재 단어와 한 글자만 다르면 이동 가능
            diff = 0

            for a, b in zip(current, word):
                if a != b:
                    diff += 1

            if diff == 1:
                visited[i] = True
                queue.append((word, count + 1))

    return 0