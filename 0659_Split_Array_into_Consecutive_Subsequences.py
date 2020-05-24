class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        '''Greedy. Time = Space = O(n)'''
        from collections import Counter
        counter_nums = Counter(nums)
        counter_tails = Counter()
        for num in nums:
            if counter_nums[num] == 0:
                continue
            if counter_tails[num] > 0:
                counter_tails[num] -= 1
                counter_tails[num + 1] += 1
            elif counter_nums[num + 1] > 0 and counter_nums[num + 2] > 0:
                counter_nums[num + 1] -= 1
                counter_nums[num + 2] -= 1
                counter_tails[num + 3] += 1
            else:
                return False
            counter_nums[num] -= 1
        return True