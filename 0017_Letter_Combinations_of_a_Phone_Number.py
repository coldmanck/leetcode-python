# Runtime: 31 ms, faster than 88.94% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14 MB, less than 34.21% of Python3 online submissions for Letter Combinations of a Phone Number.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # time complexity: O(4^N * N)
        # space complexity: O(N)
        ans = []
        digit_to_chs = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z'),
        }
        
        def helper(i, cur_ans):
            if i == len(digits):
                if len(cur_ans) != 0:
                    ans.append(''.join(cur_ans))
                return
            for ch in digit_to_chs[digits[i]]:
                helper(i + 1, cur_ans + [ch])
        
        helper(0, [])
        return ans