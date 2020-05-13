class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 if len(str(i)) % 2 == 0 else 0 for i in nums])