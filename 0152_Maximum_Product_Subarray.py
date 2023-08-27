class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums2 = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            nums2[i] *= nums2[i - 1] or 1
        return max(nums + nums2)

        '''
        A = [2, 3, -2, 4]
        B = [4, -2, 3, 2]
        A2 = [2, 6, -12, -48]
        B2 = [4, -8, -24, -48]
        A2+B2 = [2, 6, -12, -48, 4, -8, -24, -48]
        '''