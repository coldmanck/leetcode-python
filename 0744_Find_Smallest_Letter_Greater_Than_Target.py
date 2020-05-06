class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid
        if letters[left] > target: # check corner case: if target is smaller than all elements
            return letters[left]
        return letters[left + 1] if left + 1 != len(letters) else letters[0]