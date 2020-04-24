# Runtime: 20 ms, faster than 98.27% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.9 MB, less than 7.69% of Python3 online submissions for Pascal's Triangle II.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''memory-efficient DP: Time O(k^2) Space O(k)'''
        ans = [1] * (rowIndex + 1)
        for row in range(2, rowIndex + 1):
            for col in range(row - 1, 0, -1):
                ans[col] += ans[col-1]
        return ans