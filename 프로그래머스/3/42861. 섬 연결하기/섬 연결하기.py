def solution(n, costs):
    answer = 0

    # 부모 노드 저장
    parent = [i for i in range(n)]

    # 루트 노드 찾기
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # 두 집합 연결
    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a
            return True

        return False

    # 비용이 작은 다리부터 확인
    costs.sort(key=lambda x: x[2])

    count = 0

    for island1, island2, cost in costs:

        # 두 섬이 아직 연결되어 있지 않다면
        if union(island1, island2):
            answer += cost
            count += 1

        # n개의 섬을 모두 연결하려면
        # 다리는 n-1개면 충분
        if count == n - 1:
            break

    return answer