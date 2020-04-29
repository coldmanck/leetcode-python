class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force: O(n^2) time
        # max_area = 0
        # for left in range(len(heights)):
        #     min_height = float('inf')
        #     for right in range(left, len(heights)):
        #         min_height = min(min_height, heights[right])
        #         max_area = max(max_area, min_height * (right - left + 1))
        # return max_area
        
        # Stack solution
        # time = space = O(n) 
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                max_area = max(max_area, (i - stack[-1] - 1) * height)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            max_area = max(max_area, (len(heights) - stack[-1] - 1) * height)
        
        return max_area