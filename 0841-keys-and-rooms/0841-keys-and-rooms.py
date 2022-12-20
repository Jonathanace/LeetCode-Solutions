class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = deque()
        visited = {0}
        for key in rooms[0]:
            stack.append(key)
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                for key in rooms[cur]:
                    stack.append(key)
                    
        # print(set([i for i in range(len(rooms))]))
        # print(visited)
        return set([i for i in range(len(rooms))]) == visited