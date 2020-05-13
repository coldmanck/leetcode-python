class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[0] >= 0 and A[-1] >= 0:
            return [a ** 2 for a in A]
        elif A[0] <= 0 and A[-1] <= 0:
            return [a ** 2 for a in A][::-1]
        else:
            i = 0
            while i < len(A) - 1 and A[i] < 0 and A[i + 1] < 0:
                i += 1
            left, right = i, i + 1
            ans = []
            while left >= 0 and right < len(A):
                if -A[left] <= A[right]:
                    ans.append(A[left] ** 2)
                    left -= 1
                else:
                    ans.append(A[right] ** 2)
                    right += 1
            if left != -1:
                ans.extend([A[i] ** 2 for i in range(left, -1, -1)])
            else:
                ans.extend([A[i] ** 2 for i in range(right, len(A))])
            return ans