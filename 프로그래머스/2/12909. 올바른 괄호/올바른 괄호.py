def solution(s):
    count = 0
    
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False
    
    return count == 0