from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0

    # 다리 위 상태
    bridge = deque([0] * bridge_length)

    # 현재 다리 위 트럭들의 총 무게
    current_weight = 0

    # 다음에 들어올 트럭의 위치
    index = 0

    while index < len(truck_weights) or current_weight > 0:
        # 1초 경과
        time += 1

        # 다리 맨 앞의 트럭이 빠져나감
        out = bridge.popleft()
        current_weight -= out

        # 아직 대기 트럭이 있다면
        if index < len(truck_weights):
            next_truck = truck_weights[index]

            # 새 트럭을 다리에 올릴 수 있는 경우
            if current_weight + next_truck <= weight:
                bridge.append(next_truck)
                current_weight += next_truck
                index += 1

            # 무게 때문에 못 올라가는 경우
            else:
                bridge.append(0)

        # 대기 트럭이 모두 올라간 경우
        else:
            bridge.append(0)

    return time