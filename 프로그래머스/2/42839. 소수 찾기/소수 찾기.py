from math import isqrt
from itertools import permutations

def solution(numbers):
    answer = 0
    candidate = []
    
    def is_prime(number):
        if number < 2:
            return 0
        for d in range(2, isqrt(number)+1):
            if number % d == 0:
                return 0
        return 1
    
    for i in range(len(numbers)):
        for num in permutations(numbers, i+1):
            candidate.append(int(''.join(num)))
    
    candidate = set(candidate)    
    for num in candidate:
        answer += is_prime(num)
    
    return answer