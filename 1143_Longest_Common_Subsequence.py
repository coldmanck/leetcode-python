class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''Brute-force recursive (TLE)'''
        # def lcs(idx1, idx2):
        #     if idx1 == len(text1) or idx2 == len(text2):
        #         return 0
        #     if text1[idx1] == text2[idx2]:
        #         return 1 + lcs(idx1 + 1, idx2 + 1)
        #     return max(lcs(idx1 + 1, idx2), lcs(idx1, idx2 + 1))
        # return lcs(0, 0)
    
        '''Recursion with memoization'''
        # from collections import defaultdict
        # memo = defaultdict(dict)
        # def lcs(idx1, idx2):
        #     if idx1 == len(text1) or idx2 == len(text2):
        #         return 0
        #     if idx1 not in memo or idx2 not in memo[idx1]:
        #         if text1[idx1] == text2[idx2]:
        #             memo[idx1][idx2] = 1 + lcs(idx1 + 1, idx2 + 1)
        #         else:
        #             memo[idx1][idx2] = max(lcs(idx1 + 1, idx2), lcs(idx1, idx2 + 1))
        #     return memo[idx1][idx2]
        # return lcs(0, 0)
        
        '''Bottom-up DP-1: time O(mn) space O(mn)'''
        # dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        # for i in range(1, len(dp)):
        #     for j in range(1, len(dp[0])):
        #         if text1[i - 1] == text2[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # return dp[-1][-1]
        
        '''Bottom-up DP-2: time O(mn) space O(min(m, n))'''
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0 for _ in range(len(text2) + 1)]
        for i in range(1, len(text1) + 1):
            dp_j_minus_1 = dp[0]
            for j in range(1, len(text2) + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = 1 + dp_j_minus_1 # dp[j - 1]
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                dp_j_minus_1 = temp
        return dp[-1]