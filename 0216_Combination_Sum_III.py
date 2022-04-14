class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Runtime: 38 ms, faster than 72.96% of Python3 online submissions for Combination Sum III.
        # Memory Usage: 13.9 MB, less than 81.62% of Python3 online submissions for Combination Sum III.
        # time complexity: O(C(9,k)) = O(9!/(k! * (9-k)!)
        # space complexity: O(k)
        ans = []
        def helper(i, cur_ans):
            if sum(cur_ans) == n and len(cur_ans) == k:
                ans.append(cur_ans)
                return
            if sum(cur_ans) > n or len(cur_ans) > k or i > 9:
                return
            helper(i + 1, cur_ans + [i])
            helper(i + 1, cur_ans)
        helper(1, [])
        return ans