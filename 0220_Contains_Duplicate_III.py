class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Worst time O(n^2/2)
        # for row in range(1, k + 1):
        #     i, j = row, 0
        #     while i < len(nums):
        #         if abs(nums[i] - nums[j]) <= t:
        #             return True
        #         i += 1
        #         j += 1
        # return False
        
        # Idea inspired by Bucket sort
        # Time O(n) Space O(k)
        # https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets
        bucket = {}
        size_of_bucket = max(1, t)
        for idx in range(len(nums)):
            bucket_idx = nums[idx] // size_of_bucket
            for b_idx in (bucket_idx - 1, bucket_idx, bucket_idx + 1):
                if b_idx in bucket and abs(bucket[b_idx] - nums[idx]) <= t:
                    return True
            # replace the bucket element with the newest element
            # (no need to store all elements)
            bucket[bucket_idx] = nums[idx]
            # remove the bucket elements farther than k w.r.t. the idx
            if idx >= k:
                bucket_idx_to_delete = nums[idx - k] // size_of_bucket
                del bucket[bucket_idx_to_delete]
        return False