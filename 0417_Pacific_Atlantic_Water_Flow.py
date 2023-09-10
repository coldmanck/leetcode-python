class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        n_rows, n_cols = len(heights), len(heights[0])
        p_visited, a_visited = set(), set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for ii, jj in directions:
                i2, j2 = i + ii, j + jj
                if 0 <= i2 < n_rows and 0 <= j2 < n_cols:
                    if heights[i2][j2] >= heights[i][j]:
                        dfs(i2, j2, visited)

        for row in range(n_rows):
            dfs(row, 0, p_visited)
            dfs(row, n_cols - 1, a_visited)
        for col in range(n_cols):
            dfs(0, col, p_visited)
            dfs(n_rows - 1, col, a_visited)
        
        return list(p_visited & a_visited)