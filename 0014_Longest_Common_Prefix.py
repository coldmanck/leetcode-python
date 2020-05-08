class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ans = []
        i = 0
        while all([i < len(s) for s in strs]):
            ch = strs[0][i]
            if all([s[i] == ch for s in strs]):
                ans.append(ch)
            else:
                break
            i += 1
        return ''.join(ans)