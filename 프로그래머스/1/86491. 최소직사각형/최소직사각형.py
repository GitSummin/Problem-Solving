def solution(sizes):
    
    # 긴 길이를 가로로
    # 짧은 길이를 세로로
    long_lst = []
    short_lst = []
    
    for w, h in sizes:
        long_lst.append(max(w, h))
        short_lst.append(min(w, h))
    
    result = max(long_lst) * max(short_lst)
    
    return result