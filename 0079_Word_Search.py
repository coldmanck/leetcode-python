class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(R×C×4^L)
        # space: O(4L)
        def dfs(i, j, word_i, visited):
            if board[i][j] != word[word_i]:
                return False
            if word_i == len(word) - 1:
                return True
            visited.add((i, j))
            for d_i, d_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + d_i, j + d_j
                if i2 < 0 or i2 >= len(board) or j2 < 0 or j2 >= len(board[0]) or (i2, j2) in visited:
                    continue
                if dfs(i + d_i, j + d_j, word_i + 1, visited):
                    return True
            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True

        return False