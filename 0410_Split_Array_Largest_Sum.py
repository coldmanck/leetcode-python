class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Time O(nlog(sum(n)-max(n))
        def is_valid(mid):
            cur_sum = count = 0
            for num in nums:
                cur_sum += num
                if cur_sum > mid:
                    cur_sum = num
                    count += 1
                    if count == m:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if not is_valid(mid):
                left = mid + 1
            else:
                right = mid
        return left