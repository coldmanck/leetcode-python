class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
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
        '''

        ans = []
        for i in range(min([len(s) for s in strs])):
            x = [s[i] for s in strs]
            if not x or not x.count(x[0]) == len(x): # check if all elements are equal
                break
            else:
                ans.append(x[0])
        return ''.join(ans)