def solution(genres, plays):
    answer = []

    sing_dict = {}
    genre_total = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별로 (고유번호, 재생횟수) 저장
        if genre not in sing_dict:
            sing_dict[genre] = [(i, play)]
        else:
            sing_dict[genre].append((i, play))

        # 장르별 총 재생횟수
        genre_total[genre] = genre_total.get(genre, 0) + play

    # 총 재생횟수가 높은 장르부터
    sorted_genres = sorted(
        genre_total,
        key=lambda x: genre_total[x],
        reverse=True
    )

    for genre in sorted_genres:

        # 장르 내에서
        # 재생횟수 내림차순, 고유번호 오름차순
        songs = sorted(
            sing_dict[genre],
            key=lambda x: (-x[1], x[0])
        )

        # 최대 2곡 선택
        for index, play in songs[:2]:
            answer.append(index)

    return answer