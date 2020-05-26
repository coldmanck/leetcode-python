class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # O(n^2) time O(n) space
        # cum_nums = [0]
        # cum = 0
        # for num in nums:
        #     cum += num
        #     cum_nums.append(cum)
        # max_count = 0
        # for i in range(len(cum_nums) - 2):
        #     for j in range(i + 2, len(cum_nums), 2):
        #         if j - i == 2 * (cum_nums[j] - cum_nums[i]) and (j - i) > max_count:
        #             max_count = j - i
        # return max_count
        
        # O(1) time O(n) space: 1 then add 1, 0 then subtract 1
        from collections import defaultdict
        table = defaultdict(list) # key of count; value of indexes
        table[0].append(0)
        max_len = 0
        count = 0
        for i, num in enumerate(nums):
            count = count + 1 if num == 1 else count - 1
            table[count].append(i + 1)
            if len(table[count]) > 1 and table[count][-1] - table[count][0] > max_len:
                max_len = table[count][-1] - table[count][0]
        return max_len