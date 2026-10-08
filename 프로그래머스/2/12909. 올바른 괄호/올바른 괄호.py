def solution(s):
    stack = []
    
    for word in s:            
        if word == "(":
            stack.append(word)
        else:
            if not stack:
                return False
            stack.pop()
            
    return len(stack) == 0