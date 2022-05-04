class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''time O(n**2): TLE'''
        # ans = 0
        # for i in range(len(arr)):
        #     cur_min = arr[i]
        #     for j in range(i, len(arr)):
        #         cur_min = min(cur_min, arr[j])
        #         ans += cur_min
        # return ans % (10**9 + 7)
        
        '''time O(n) using monotone (monotonous increase) stack'''
        # Runtime: 722 ms, faster than 27.77% of Python3 online submissions for Sum of Subarray Minimums.
        # Memory Usage: 19 MB, less than 42.00% of Python3 online submissions for Sum of Subarray Minimums.
        ans = 0
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                cur_min_idx = stack.pop()
                ans += arr[cur_min_idx] * (i - cur_min_idx) * (cur_min_idx - stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)