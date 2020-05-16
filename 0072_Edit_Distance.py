class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        if A[a-1] == B[b-1]: E(A[0:a-1], B[0:b-1]) = E(A[0:a-2], B[0:b-2])
        else:                E(A[0:a-1], B[0:b-1]) = 1 + min(E(A[0:a-2], B[0:b-2]), # replace
                                                               A[0:a-1], B[0:b-2]), # add B[b-1] to A
                                                               A[0:a-2], B[0:b-1])) # delete A[a-1]
        '''
        A, B = word1, word2
        cache = [[-1 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        cache[0] = [i for i in range(len(B) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(len(B) + 1):
                if j == 0:
                    cache[i][j] = i
                elif A[i - 1] == B[j - 1]:
                    cache[i][j] = cache[i - 1][j - 1]
                else:
                    cache[i][j] = 1 + min(cache[i - 1][j - 1], cache[i - 1][j], cache[i][j - 1])
        return cache[-1][-1]