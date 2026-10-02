def solution(fees, records):
    answer = []
    
    default_time, default_fee, unit_time, unit_fee = fees

    in_time = {}
    total_time = {}
    
    def to_minute(time):
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute
    
    # 입출차 기록 처리
    for record in records:
        time, car, op = record.split()
        
        if op == "IN":
            in_time[car] = to_minute(time)
        
        else:
            parking_time = to_minute(time) - in_time[car]
            total_time[car] = total_time.get(car, 0) + parking_time
            del in_time[car]
    
    # 출차 기록이 없는 차량은 23:59에 출차한 것으로 처리
    for car in in_time:
        parking_time = to_minute("23:59") - in_time[car]
        total_time[car] = total_time.get(car, 0) + parking_time
    
    # 차량 번호가 작은 순서대로 요금 계산
    for car in sorted(total_time):
        parking_time = total_time[car]
        
        # 기본 시간 이하
        if parking_time <= default_time:
            fee = default_fee
        
        # 기본 시간 초과
        else:
            extra_time = parking_time - default_time
            
            # 초과 시간을 단위 시간으로 올림
            unit_count = (extra_time + unit_time - 1) // unit_time
            
            fee = default_fee + unit_count * unit_fee
        
        answer.append(fee)
    
    return answer