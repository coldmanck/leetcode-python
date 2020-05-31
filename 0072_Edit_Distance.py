class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        if A[a-1] == B[b-1]: E(A[0:a-1], B[0:b-1]) = E(A[0:a-2], B[0:b-2])
        else:                E(A[0:a-1], B[0:b-1]) = 1 + min(E(A[0:a-2], B[0:b-2]), # replace
                                                               A[0:a-1], B[0:b-2]), # add B[b-1] to A
                                                               A[0:a-2], B[0:b-1])) # delete A[a-1]
        '''
        '''DP with 2D cache: O(mn) time & space'''
        # dp = [[i for i in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # for i in range(1, len(word1) + 1):
        #     for j in range(len(word2) + 1):
        #         if j == 0:
        #             dp[i][j] = i
        #         elif word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        # return dp[-1][-1]
        
        '''DP with 1D cache: O(mn) time, O(min(m, n)) space'''
        if len(word2) > len(word1):
            word1, word2 = word2, word1
        dp = [i for i in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(len(word2) + 1):
                if j == 0:
                    dp_j_minus_1 = dp[j]
                    dp[j] = i
                    continue
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = dp_j_minus_1
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], dp_j_minus_1)
                dp_j_minus_1 = temp
        return dp[-1]