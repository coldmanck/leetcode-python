class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        from collections import Counter
        c_s = Counter(s[:len(p)])
        c_p = Counter(p)
        ans = [0] if c_s == c_p else []
        for i in range(len(p), len(s)):
            c_s[s[i]] += 1
            c_s[s[i - len(p)]] -= 1
            if c_s[s[i - len(p)]] == 0:
                del c_s[s[i - len(p)]]
            if c_s == c_p:
                ans.append(i - len(p) + 1)
        return ans