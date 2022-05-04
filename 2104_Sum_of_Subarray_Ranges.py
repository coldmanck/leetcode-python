class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        '''Time O(n**2)'''
        # ans = 0
        # for i in range(len(nums) - 1):
        #     min_num = max_num = nums[i]
        #     for j in range(i, len(nums)):
        #         min_num = min(min_num, nums[j])
        #         max_num = max(max_num, nums[j])
        #         ans += max_num - min_num
        # return ans
        
        '''Time O(n) using monotonic stack'''
        ans = 0 
        
        # Sum of Subarray Minimums
        new_nums = [float('-inf')] + nums + [float('-inf')]
        stack = [] # monotonic increasing stack
        for i in range(len(new_nums)):
            while stack and new_nums[stack[-1]] > new_nums[i]:
                cur_min_idx = stack.pop()
                ans -= new_nums[cur_min_idx] * (i - cur_min_idx) * (cur_min_idx - stack[-1])
            stack.append(i)
        
        # Sum of Subarray Maximums
        new_nums = [float('inf')] + nums + [float('inf')]
        stack = [] # monotonic decreasing stack
        for i in range(len(new_nums)):
            while stack and new_nums[stack[-1]] < new_nums[i]:
                cur_min_idx = stack.pop()
                ans += new_nums[cur_min_idx] * (i - cur_min_idx) * (cur_min_idx - stack[-1])
            stack.append(i)
        
        return ans