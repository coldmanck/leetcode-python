class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # time O(min(len(s), len(t))) space O(1)
        ps = pt = 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps == len(s)