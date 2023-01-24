class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # O(n) time O(n) space
        '''
        def final_str(s):
            temp = []
            for ch in s:
                if ch == '#':
                    if len(temp) > 0:
                        temp.pop()
                else:
                    temp.append(ch)
            return temp
        return final_str(s) == final_str(t)
        '''

        # O(n) time O(1) space
        i, j = len(s) - 1, len(t) - 1
        back_s = back_t = 0
        while True:
            while i >= 0 and (back_s > 0 or s[i] == '#'): # compute the skips for str s
                back_s += 1 if s[i] == '#' else -1
                i -= 1
            while j >= 0 and (back_t > 0 or t[j] == '#'): # compute the skips for str t
                back_t += 1 if t[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and s[i] == t[j]): # compare s[i] to t[j]
                return i == j == -1
            i, j = i - 1, j - 1