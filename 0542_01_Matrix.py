class Solution:
    # Solution reference: https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        queue = deque()
        visited = set()
        length, width = len(matrix), len(matrix[0])
        for i in range(length):
            for j in range(width):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
        
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while queue:
            i, j = queue.popleft()
            for ii, jj in directions:
                i2, j2 = i + ii, j + jj
                if 0 <= i2 < length and 0 <= j2 < width and (i2, j2) not in visited:
                    visited.add((i2, j2))
                    queue.append((i2, j2))
                    matrix[i2][j2] = matrix[i][j] + 1
        
        return matrix