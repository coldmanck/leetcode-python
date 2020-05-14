class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''factorial divmod: time O(n) space O(n)'''
        cache = {}
        def fact(x):
            if x == 0 or x == 1:
                return 1
            if not x in cache:
                cache[x] = fact(x - 1) * x
            return cache[x]
        
        nums = [i for i in range(1, n + 1)]
        ans = []
        cur_n = n
        k -= 1 # to 0 index based
        while len(ans) < n:
            d = k // fact(cur_n - 1)
            ans.append(str(nums[d]))
            del nums[d]
            k %= fact(cur_n - 1)
            cur_n -= 1
        return ''.join(ans)
        
        '''TLE: time O(n!) space O(n)'''
        '''
        nums = [i for i in range(1, n + 1)]
        
        def permutate(i, cur_ans, nums, ans):
            if i == n:
                ans.append(cur_ans)
                if len(ans) == k:
                    return True
                return False
            for j in range(len(nums)):
                if permutate(i + 1, cur_ans + [nums[j]], nums[:j] + nums[j+1:], ans):
                    return True
                
        ans = []
        permutate(0, [], nums, ans)
        return ''.join([str(i) for i in ans[k - 1]])
        '''