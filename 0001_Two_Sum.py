# Runtime: 56 ms, faster than 38.91% of Python3 online submissions for Two Sum.
# Memory Usage: 15.6 MB, less than 5.11% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Method 1: Hash table. Time O(n) Space O(n)'''
        dic = {} # key of the complement element that we are finding, value of the original element's idx
        for idx in range(len(nums)):
            if nums[idx] in dic:
                return [dic[nums[idx]], idx]
            dic[target - nums[idx]] = idx
        
        '''Method 2: Sorting. Time O(nlogn) Space O(n)'''
        # left, right = 0, len(nums) - 1
        # sorted_nums = sorted([(nums[idx], idx) for idx in range(len(nums))])
        # while left < right:
        #     cur_sum = sorted_nums[left][0] + sorted_nums[right][0]
        #     if cur_sum == target:
        #         return [sorted_nums[left][1], sorted_nums[right][1]]
        #     elif cur_sum < target:
        #         left += 1
        #     else:
        #         right -= 1