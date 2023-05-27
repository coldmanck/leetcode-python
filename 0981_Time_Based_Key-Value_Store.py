from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or timestamp < self.map[key][0][0]: # do check the corner case
            return ''
        
        # bisect_right to find the nearest value
        left, right = 0, len(self.map[key]) - 1
        while left < right:
            mid = (left + right) // 2 + 1 # be ware of this +1
            if timestamp < self.map[key][mid][0]:
                right = mid - 1
            else:
                left = mid
        return self.map[key][right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)