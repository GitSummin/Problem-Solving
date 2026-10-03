def solution(brown, yellow):
    # 가로 × 세로 = brown + yellow
    total = brown + yellow

    for height in range(3, total + 1):
        if total % height == 0:
            width = total // height

            if width >= height:
                # (가로 - 2) × (세로 - 2) = yellow
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]