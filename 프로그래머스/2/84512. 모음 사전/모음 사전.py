def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []

    def dfs(current):
        # 빈 문자열은 사전에 없으므로 제외
        if current:
            words.append(current)
        # 길이가 5가 되면 더 이상 문자 추가하지 않음
        if len(current) == 5:
            return
        # A, E, I, O, U 순서대로 붙이기
        for vowel in vowels:
            dfs(current + vowel)

    dfs("")

    # index는 0부터 시작하므로 +1
    return words.index(word) + 1