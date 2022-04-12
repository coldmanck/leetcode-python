class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/C%2B%2BJavaPython-One-pass-O(N)
        import string
        idxs = {ch:[-1, -1] for ch in string.ascii_uppercase}
        ans = 0
        for idx, ch in enumerate(s):
            i, j = idxs[ch]
            ans += (idx - j) * (j - i)
            idxs[ch] = [j, idx]
        for ch, (i, j) in idxs.items():
            ans += (len(s) - j) * (j - i)
        return ans