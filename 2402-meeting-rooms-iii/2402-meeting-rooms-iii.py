from heapq import heapify, heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked_rooms = [] # [end_time, room_i]
        free_rooms = list(range(n)) # room_i
        rooms_book_count = [0 for room_i in range(n)] # [count, room_i]

        meetings.sort()

        for start, end in meetings:    
            # free up booked rooms
            while booked_rooms and booked_rooms[0][0] <= start:
                free_room = heappop(booked_rooms)[1]
                heappush(free_rooms, free_room)

            if free_rooms: # Always use free room if available 
                room_i = heappop(free_rooms)
                heappush(booked_rooms, [end, room_i])

            elif not free_rooms: # Use next free room if all rooms are booked
                duration = end - start
                earliest_end, room_i = heappop(booked_rooms)
                new_end = earliest_end + duration
                heappush(booked_rooms, [new_end, room_i])

            rooms_book_count[room_i] += 1 # Increment book count
        
        return rooms_book_count.index(max(rooms_book_count)) # Return room with max count
