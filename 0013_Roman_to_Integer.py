class Solution:
    def romanToInt(self, s: str) -> int:
        ans = i = 0
        cache1 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        cache2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < len(s):
            if i == len(s) - 1 or s[i:i + 2] not in cache1:
                ans += cache2[s[i]]
                i += 1
            else:
                ans += cache1[s[i:i + 2]]
                i += 2
        return ans