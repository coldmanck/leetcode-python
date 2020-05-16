class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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