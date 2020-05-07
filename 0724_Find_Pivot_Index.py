class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        
        # create a cumulative array
        cu = [-1] * len(nums)
        cu[0] = nums[0]
        for i in range(1, len(nums)):
            cu[i] = cu[i - 1] + nums[i]
        
        # the idx is at c[-1] - c[idx] == c[idx - 1]
        for i in range(len(cu)):
            if i == 0:
                if cu[-1] - cu[i] == 0:
                    return i
            else:
                if cu[-1] - cu[i] == cu[i - 1]:
                    return i
        return -1