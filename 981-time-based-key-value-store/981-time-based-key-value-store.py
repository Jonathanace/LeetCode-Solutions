class TimeMap:

    def __init__(self):
        self.l = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp >= len(self.l):
            for i in range(timestamp - len(self.l)):
                self.l.append({})
            self.l.append({key: value})
        else:
            self.l[timestamp][key] = value
        # print(key, value, timestamp, self.l)

    def get(self, key: str, timestamp: int) -> str:
        # print(key, timestamp)
        # print(self.l)
        for i in range(min(timestamp, len(self.l)-1), 0, -1):
            # print('     ', i)
            if key in self.l[i]:
                return self.l[i][key]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)