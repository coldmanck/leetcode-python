class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # longest common subsequence
        '''Method 1: naive recursion: time = O( 2 ^ max(len(A), len(B)) ) space O(1)'''
        # def lcs(a, b):
        #     if a == len(A) or b == len(B):
        #         return 0
        #     if A[a] == B[b]:
        #         return 1 + lcs(a + 1, b + 1)
        #     return max(lcs(a + 1, b), lcs(a, b + 1))
        # return lcs(0, 0)
        
        '''Method 2: recursion with memo (DP): time = space = O(len(A) * len(B))'''
        cache = {} # key of (a, b) value of number of possible answer
        def lcs(a, b):
            if a == len(A) or b == len(B):
                return 0
            if (a, b) not in cache:
                cache[(a, b)] = 1 + lcs(a + 1, b + 1) if A[a] == B[b] else max(lcs(a + 1, b), lcs(a, b + 1))
            return cache[(a, b)]
        return lcs(0, 0)