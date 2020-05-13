class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = [-1] * len(A)
        even, odd = 0, len(A) - 1
        for num in A:
            if num % 2 == 0:
                ans[even] = num
                even += 1
            else:
                ans[odd] = num
                odd -= 1
        return ans