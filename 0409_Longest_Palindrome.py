class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_set = set()
        ans = 0
        for ch in s:
            if ch in ch_set:
                ans += 2
                ch_set.remove(ch)
            else:
                ch_set.add(ch)
        return ans + 1 if ch_set else ans