# Runtime: 84 ms, faster than 54.56% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Palindrome Partitioning.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # method 1:
        # 1. generate all possible partitioning: O(2^n) time
        # 2. check if they satisify palindrome: O(n) each
        
        # method 2: backtrack
        if not s:
            return []
        ans = []
        def helper(s, cur_ans):
            if len(s) == 0:
                ans.append(cur_ans)
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[i-1::-1]:
                    helper(s[i:], cur_ans + [s[:i]])
        
        helper(s, [])
        return ans