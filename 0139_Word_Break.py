# Runtime: 40 ms, faster than 55.92% of Python3 online submissions for Word Break.
# Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Word Break.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''Method 1: recursion (TLE)'''
        '''Method 2: recursion + memoization
        Time O(n^2) Space O(n)
        '''
        '''
        def word_break(idx, s, memo):
            if idx == len(s):
                return True
            if idx in memo:
                return memo[idx]
            
            end_idx = idx
            while end_idx < len(s):
                if s[idx:end_idx + 1] in wordDict and word_break(end_idx + 1, s, memo):
                    memo[idx] = True
                    return memo[idx]
                end_idx += 1
            memo[idx] = False
            return memo[idx]
        
        return word_break(0, s, {})
        '''
        '''Method 3: DP'''
        cache = [False] * (len(s) + 1)
        cache[0] = True
        set_wordDict = set(wordDict)
        for i in range(1, len(cache)):
            for j in range(0, i):
                if cache[j] and s[j:i] in set_wordDict:
                    cache[i] = True
                    break
        
        return cache[-1]