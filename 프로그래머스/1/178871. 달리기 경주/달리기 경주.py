def solution(players, callings):    
    rank_dict = {}
    
    for i, player in enumerate(players):
        rank_dict[player] = i
    
    for call in callings:
        rank = rank_dict[call]
        front_player = players[rank-1]
        
        players[rank-1], players[rank] = players[rank], players[rank-1]
        
        rank_dict[call] -= 1
        rank_dict[front_player] += 1
    
    return players