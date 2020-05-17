class Solution:
    def countBits(self, num: int) -> List[int]:
        '''Method 1'''
        # ans = []
        # for i in range(num + 1):
        #     ans.append(sum([ch == '1' for ch in bin(i)]))
        # return ans
        
        '''Method 2'''
        # two_powers = set()
        # ans = []
        # power = 2
        # count = -1
        # for i in range(num + 1):
        #     if i >= power and i not in two_powers:
        #         two_powers.add(i)
        #         power *= 2
        #     count += 1
        #     for p in two_powers:
        #         if i % p == 0:
        #             count -= 1
        #     ans.append(count)
        # return ans
        
        '''Method 3: DP'''
        # dp[i] = dp[i - offset] + 1
        offset = 1
        dp = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            if i >= 2 * offset:
                offset *= 2
            dp[i] = dp[i - offset] + 1
        return dp