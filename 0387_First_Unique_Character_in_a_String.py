# Runtime: 140 ms, faster than 37.54% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.

from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        for i in range(len(s)):
            d[s[i]] = (2, i) if s[i] in d else (1, i)
        # print(d)
        for k, v in d.items():
            if v[0] == 1:
                return v[1]
        return -1