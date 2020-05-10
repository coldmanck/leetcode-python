class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''stack time O(n) space O(n)'''
        if not T:
            return []
        stack = [(T[0], 0)]
        ans = [0] * len(T)
        for i in range(1, len(T)):
            while stack and T[i] > stack[-1][0]:
                t2, t2_i = stack.pop()
                ans[t2_i] = i - t2_i
            stack.append((T[i], i))
        return ans
            
        
        '''Brute-force O(n^2) solution'''
        # ans = [0] * len(T)
        # for i in range(len(T) - 1): # for only idx 0 to len(T) - 2
        #     for j in range(i + 1, len(T)):
        #         if T[i] < T[j]:
        #             ans[i] = j - i
        #             break
        # return ans