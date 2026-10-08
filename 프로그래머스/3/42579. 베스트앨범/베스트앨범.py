def solution(genres, plays):
    answer = []
    
    sing_dict = {}
    genre_total = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if not genre in sing_dict:
            sing_dict[genre] = [(i, play)]
        else:
            sing_dict[genre].append((i, play))
        
        genre_total[genre] = genre_total.get(genre, 0) + play
        
    sorted_genres = sorted(genre_total, key=lambda x: genre_total[x], reverse=True)
    
    for genre in sorted_genres:
        songs = sorted(sing_dict[genre], key=lambda x: (-x[1], x[0]))
        
        for index, play in songs[:2]:
            answer.append(index)
            
    return answer