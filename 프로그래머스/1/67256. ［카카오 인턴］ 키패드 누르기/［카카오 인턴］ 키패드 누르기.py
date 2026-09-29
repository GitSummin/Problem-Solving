def solution(numbers, hand):
    answer = ''

    left_number = [1, 4, 7]
    right_number = [3, 6, 9]

    position = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    # 처음 손 위치
    left_pos = '*'
    right_pos = '#'

    for number in numbers:

        # 왼쪽 열
        if number in left_number:
            answer += 'L'
            left_pos = number

        # 오른쪽 열
        elif number in right_number:
            answer += 'R'
            right_pos = number

        # 가운데 열
        else:
            lx, ly = position[left_pos]
            rx, ry = position[right_pos]
            nx, ny = position[number]

            left_distance = abs(lx - nx) + abs(ly - ny)
            right_distance = abs(rx - nx) + abs(ry - ny)

            if left_distance < right_distance:
                answer += 'L'
                left_pos = number

            elif right_distance < left_distance:
                answer += 'R'
                right_pos = number

            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = number
                else:
                    answer += 'R'
                    right_pos = number

    return answer