class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''Dictionary. Time O(n) space O(n)'''
        # from collections import Counter
        # counts = Counter(nums)
        # return max(counts.keys(), key=counts.get)
        
        '''Sorting. Time O(nlogn) space O(1)'''
        # return sorted(nums)[len(nums) // 2]
        
        '''Boyer-Moore Voting Algorithm. '''
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate