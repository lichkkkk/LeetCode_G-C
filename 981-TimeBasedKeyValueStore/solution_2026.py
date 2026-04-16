import bisect

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        idx = bisect.bisect_left(self.map[key], timestamp, key=lambda x: x[0])
        if idx < len(self.map[key]) and self.map[key][idx][0] == timestamp:
            return self.map[key][idx][1]
        if idx == 0:
            return ''
        return self.map[key][idx-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
