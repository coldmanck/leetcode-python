class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # can be factorized nums[j] + nums[k] == -nums[i]
        if len(nums) <= 2:
            return []
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            target = -nums[i]
            value_needed = set()
            for j in range(i + 1, len(nums)):
                if target - nums[j] in value_needed:
                    ans.add(
                        ((-target, target - nums[j], nums[j]))
                    )
                else:
                    value_needed.add(nums[j])
        return list(ans)
        # time: O(n**2 + nlogn) = O(n**2)
        # space: O(n) for python's sorted or O(nlogn) depends on the sorting algo. used
        
        # binary search?
        '''
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 2:
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[left] + nums[right]
                if cur == -nums[i]:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur < -nums[i]:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return ans
        '''
        
        # recursion method: O(2^n)
        '''
        if len(nums) < 2:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        
        ans = []
        def three_sum(nums, idx, ans):
            if idx == 3:
                sol = sum(nums[:3])
                if sol == 0:
                    ans.append(nums[:3])
                    val = sorted(nums[:3])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                three_sum(nums, idx + 1, ans)
                nums[idx], nums[i] = nums[i], nums[idx]
        three_sum(nums, 0, ans)
        return ans
        '''
        