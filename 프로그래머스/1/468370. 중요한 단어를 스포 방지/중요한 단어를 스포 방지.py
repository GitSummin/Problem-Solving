
def solution(message, spoiler_ranges):
    words = []
    
    start = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            words.append((start, i - 1, message[start:i]))
            start = i + 1

    normal_words = set()
    spoiler_words = set()
    
    for s, e, word in words:
        is_spoiler = False
        
        for a, b in spoiler_ranges:
            if s <= b and e >= a:
                is_spoiler = True
                break
        
        if is_spoiler:
            spoiler_words.add(word)
        else:
            normal_words.add(word)

    revealed = set()
    answer = 0

    for a, b in spoiler_ranges:
        for s, e, word in words:
            if s <= b and e >= a:
                if (word not in normal_words
                    and word not in revealed):
                    answer += 1
                
                revealed.add(word)

    return answer