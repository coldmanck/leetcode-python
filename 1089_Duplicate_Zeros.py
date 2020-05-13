class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_len = len(arr) + sum([num == 0 for num in arr])
        i, j = len(arr) - 1, new_len - 1
        while j > len(arr) - 1:
            if arr[i] != 0:
                j -= 1
            else:
                j -= 2
            i -= 1
        if j != len(arr) - 1:
            arr[len(arr) - 1] = 0
            
        while i >= 0:
            if arr[i] != 0:
                arr[j] = arr[i]
                j -= 1
            else:
                arr[j] = arr[j - 1] = 0
                j -= 2
            i -= 1
        