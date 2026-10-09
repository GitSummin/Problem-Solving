def solution(genres, plays):
    answer = []
    
    genre_total = {}
    sing_dic = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if not genre in sing_dic:
            sing_dic[genre] = [(i, play)]
        else:
            sing_dic[genre].append((i, play))
        
        genre_total[genre] = genre_total.get(genre, 0) + play
            
    sorted_genre = sorted(genre_total, key=lambda x: genre_total[x], reverse=True)
    
    for genre in sorted_genre:
        sorted_sing = sorted(sing_dic[genre], key=lambda x: (x[1], -x[0]), reverse=True)
                
        for idx, sing in sorted_sing[:2]:
            answer.append(idx)
    
    return answer