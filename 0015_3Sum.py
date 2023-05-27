class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute-force: time O(n^3) space O(1)
        
        # transform into twoSum: time O(n^2) space O(n)
        # ans = set()
        # for i in range(len(nums) - 2):
        #     target_set = set()
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] in target_set:
        #             ans.add(tuple(sorted([nums[i], -nums[j]-nums[i], nums[j]])))
        #         else:
        #             target_set.add(-nums[j]-nums[i])
        # return list(ans)
        
        # two-pointer after sorting: time O(nlogn + n^2) space O(1)
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
                if left >= right:
                    break
                if nums[left] + nums[right] == -nums[i]:
                    ans.add(tuple(sorted([nums[left], nums[right], nums[i]])))
                    left, right = left + 1, right - 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return list(ans)
        
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
        