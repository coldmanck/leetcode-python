# Runtime: 436 ms, faster than 9.54% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 17.4 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        self.data.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.data:
            return False
        self.data.remove(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.data) > 0:
            return random.sample(self.data, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()