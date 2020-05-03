class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # time O(len(J) + len(S)) space O(len(set(S)))
        from collections import Counter
        dict_s = Counter(S)
        ans = 0
        for j in J:
            if j in dict_s:
                ans += dict_s[j]
        return ans