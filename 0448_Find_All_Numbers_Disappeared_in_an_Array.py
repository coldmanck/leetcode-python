class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''O(n) time O(1) space'''
        # *** Use the own index and element as the space *** 
        # mark those seen index as negative in the first pass
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        # filter out those positive idx in the second pass
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
        '''O(n) time O(n) space'''
        # return list(set(range(1, len(nums) + 1)) - set(nums))
            
        '''O(n^2) time O(1) space'''
        # ans = [i for i in range(1, len(nums) + 1)]
        # for num in nums:
        #     if num in ans:
        #         ans.remove(num)
        # return ans