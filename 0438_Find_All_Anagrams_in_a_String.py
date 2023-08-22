from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        counter_p = Counter(p)
        counter_s = Counter(s[:len(p)])
        ans = []
        if counter_s == counter_p:
            ans.append(0)
        for i in range(len(p), len(s)):
            counter_s[s[i - len(p)]] -= 1
            counter_s[s[i]] += 1
            if counter_s == counter_p:
                ans.append(i - len(p) + 1)
        return ans