# Runtime: 32 ms, faster than 24.45% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''Method 1 Memory Limit Exceeded'''
        # ans = [[1]]
        # def pascal(n):
        #     if n == 1:
        #         return
        #     last = ans[-1]
        #     if len(last) < 2:
        #         ans.append([1, 1])
        #     elif len(last) < 3:
        #         ans.append([1, 2, 1])
        #     else:
        #         mid = len(last) // 2
        #         temp = [last[i]+last[i+1] for i in range(mid)]
        #         temp_rev = temp[::-1] if len(last) % 2 == 1 else temp[len(temp)-2::-1]
        #         ans.append([1] + temp + temp_rev + [1])
        #     pascal(n-1)
        # pascal(numRows)
        # return ans

        '''Method 2 DP'''
        ans = [[1] * row for row in range(1, numRows + 1)]
        for row in range(2, numRows):
            for col in range(1, row):
                ans[row][col] = ans[row-1][col-1] + ans[row-1][col]
        return ans
        
        '''Method 3 DP'''
        # if numRows == 0:
        #     return []
        # elif numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1], [1, 1]]
        # ans = [[-1] * i for i in range(1, numRows + 1)]
        # ans[:2] = [[1], [1, 1]]
        # for row in range(2, numRows):
        #     ans[row][0] = ans[row][-1] = 1
        #     for idx in range(1, row):
        #         ans[row][idx] = ans[row-1][idx] + ans[row-1][idx-1]
            
        # return ans
    