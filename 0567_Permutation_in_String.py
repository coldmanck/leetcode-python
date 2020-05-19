from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # time O(len(s1)*len(s2)) space O(1) (26 chs)
        if len(s1) > len(s2):
            return False
        c_s1 = Counter(s1)
        c_s2 = Counter(s2[:len(s1)])
        if c_s1 == c_s2:
            return True
        for i in range(len(s1), len(s2)):
            c_s2[s2[i - len(s1)]] -= 1
            if c_s2[s2[i - len(s1)]] == 0:
                del c_s2[s2[i - len(s1)]]
            c_s2[s2[i]] += 1
            if c_s1 == c_s2:
                return True
        return False