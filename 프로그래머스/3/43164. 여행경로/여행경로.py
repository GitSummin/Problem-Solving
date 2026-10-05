def solution(tickets):
    graph = {}

    # 출발 공항별 도착 공항 저장
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    # 알파벳 순으로 작은 공항을 뒤에서 pop할 수 있도록 역순 정렬
    for start in graph:
        graph[start].sort(reverse=True)

    stack = ["ICN"]
    route = []

    while stack:
        current = stack[-1]

        # 현재 공항에서 사용할 수 있는 항공권이 남아 있다면 이동
        if current in graph and graph[current]:
            next_airport = graph[current].pop()
            stack.append(next_airport)

        # 더 이상 갈 곳이 없다면 최종 경로에 추가
        else:
            route.append(stack.pop())

    return route[::-1]