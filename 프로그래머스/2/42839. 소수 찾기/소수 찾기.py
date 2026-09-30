from itertools import permutations

def solution(numbers):
    answer = 0
    candidate = set()

    # 1. 만들 수 있는 모든 숫자 생성
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int(''.join(p))
            candidate.add(num)
            
    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True
            
    # 2. 소수 판별
    for num in candidate:
        if is_prime(num):
            answer += 1

    return answer