class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Method 1: hash table: time O(n) space O(n)
        cache = {} # key of the number which the idx is finding, value is the idx
        for i, num in enumerate(numbers):
            if num in cache:
                return [cache[num] + 1, i + 1]
            cache[target - num] = i
        
        # Method 2: two pointers: time O(n) space O(1)
        # left, right = 0, len(numbers) - 1
        # while left < right:
        #     if numbers[left] + numbers[right] == target:
        #         return left + 1, right + 1
        #     if numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         right -= 1