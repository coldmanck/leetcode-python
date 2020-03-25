# Runtime: 124 ms, faster than 73.13% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 19.6 MB, less than 96.00% of Python3 online submissions for Product of Array Except Self.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''O(n) time O(n) space'''
        # prefix, suffix = [1], [1]
        # for i, num in enumerate(nums):
        #     prefix.append(prefix[i] * num)
        # for i, num in enumerate(nums[::-1]):
        #     suffix.append(suffix[i] * num)
        # ans = []
        # for i in range(1, len(nums) + 1):
        #     ans.append(prefix[i-1] * suffix[len(nums)-i])
        # return ans
        
        '''O(n) time O(1) space'''
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = nums[i]
            else:
                answer[i] = answer[i-1] * nums[i]
        r = 1
        for i in reversed(range(len(nums))):
            if i == 0:
                answer[i] = r
            else:
                answer[i] = answer[i-1] * r
                r *= nums[i]
        return answer