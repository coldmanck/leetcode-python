# Runtime: 20 ms, faster than 97.30% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 12.9 MB, less than 98.53% of Python3 online submissions for Letter Combinations of a Phone Number.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        table = {'2':('a', 'b', 'c'), '3':('d','e','f'), '4':('g','h','i'), '5':('j','k','l'),
                 '6':('m','n','o'), '7':('p','q','r','s'), '8':('t','u','v'), '9':('w','x','y','z')}
        
        def letter_comb(s, temp_str):
            if len(s) == 0:
                ans.append(temp_str)
                return
            for ch in table[s[0]]:
                letter_comb(s[1:], temp_str + ch)
        
        letter_comb(digits, '')
        return ans