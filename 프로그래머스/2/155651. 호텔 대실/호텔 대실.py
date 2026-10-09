import heapq

def solution(book_time):
    answer = 0 
    bookings = []
    
    for time in book_time:
        start, end = time
        
        s_hour, s_minute = map(int, start.split(':'))
        e_hour, e_minute = map(int, end.split(':'))
        
        start_time = s_hour * 60 + s_minute
        end_time = e_hour * 60 + e_minute + 10
        
        bookings.append((start_time, end_time))
    
    bookings.sort()
    rooms = []
    
    for start, end in bookings:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    
    return len(rooms)