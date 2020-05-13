class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''Time O(n) space O(1) (or O(k))'''
        one = two = three = float('-inf')
        for num in nums:
            if num > one:
                one, two, three = num, one, two
            elif num < one and num > two:
                two, three = num, two
            elif num < one and num < two and num > three:
                three = num
        return three if three != float('-inf') else one
        
        '''time O(n) space O(n)'''
        # nums = list(set(nums))
        # k = 3
        # if len(nums) < k:
        #     return max(nums)
        # import heapq
        # heap = nums[:k]
        # for i in range(k, len(nums)):
        #     if nums[i] > heap[0]:
        #         heapq.heapreplace(heap, nums[i])
        # return heap[0]