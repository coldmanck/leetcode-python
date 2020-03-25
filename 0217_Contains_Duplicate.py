# Runtime: 136 ms, faster than 21.64% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.3 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ele_set = set()
        for num in nums:
            if num in ele_set:
                return True
            ele_set.add(num)
        return False