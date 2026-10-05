def solution(tickets):
    tickets.sort()

    used = [False] * len(tickets)
    route = ["ICN"]

    def dfs(current):
        # 항공권을 모두 사용했다면 정답
        if len(route) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]

            if start == current and not used[i]:
                used[i] = True
                route.append(end)

                if dfs(end):
                    return True

                # 이 경로로는 모든 항공권 사용 불가
                route.pop()
                used[i] = False

        return False

    dfs("ICN")

    return route