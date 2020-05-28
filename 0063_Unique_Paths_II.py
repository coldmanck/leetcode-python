class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        cache = []
        for i in range(len(obstacleGrid)):
            cache.append([-1 if obstacleGrid[i][j] == 1 else 0 for j in range(len(obstacleGrid[0]))])
        
        # process the first row and the first column
        i = 0
        while i < len(cache[0]) and cache[0][i] == 0:
            cache[0][i] = 1
            i += 1
        i = 1
        while i < len(cache) and cache[i][0] == 0:
            cache[i][0] = 1
            i += 1

        for i in range(1, len(cache)):
            for j in range(1, len(cache[0])):
                if cache[i][j] == -1:
                    continue
                if cache[i - 1][j] != -1:
                    cache[i][j] += cache[i - 1][j]
                if cache[i][j - 1] != -1:
                    cache[i][j] += cache[i][j - 1]

        return cache[-1][-1]