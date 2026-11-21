from math import isqrt

def solution(n):
    answer = 0
    
    def is_prime(number):
        if number < 2:
            return 0
        for num in range(2, isqrt(number) + 1):
            if number % num == 0:
                return 0
        return 1

    for num in range(1, n+1):
        answer += is_prime(num)
        
    return answer