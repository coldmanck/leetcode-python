class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS
        oldColor = image[sr][sc]
        if newColor == oldColor or not image:
            return image
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        stack = [(sr, sc)]
        while stack:
            sr, sc = stack.pop()
            image[sr][sc] = newColor
            for dr, dc in directions:
                r, c = sr + dr, sc + dc
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == oldColor:
                    stack.append((r, c))
        return image