class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''stack time O(n) space O(n)'''
        stack = [] # (temp, idx)
        ans = [0] * len(T)
        for idx, temp in enumerate(T):
            while stack and temp > stack[-1][0]:
                _, low_idx = stack.pop()
                ans[low_idx] = idx - low_idx
            stack.append((temp, idx))
        return ans
            
        
        '''Brute-force O(n^2) solution'''
        # ans = [0] * len(T)
        # for i in range(len(T) - 1): # for only idx 0 to len(T) - 2
        #     for j in range(i + 1, len(T)):
        #         if T[i] < T[j]:
        #             ans[i] = j - i
        #             break
        # return ans